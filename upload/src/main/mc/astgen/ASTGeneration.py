# from MCVisitor import MCVisitor
# from MCParser import MCParser
# from AST import *

# class ASTGeneration(MCVisitor):
#     def visitProgram(self,ctx:MCParser.ProgramContext):
#         return Program([FuncDecl(Id("main"),[],self.visit(ctx.mctype()),Block([self.visit(ctx.body())] if ctx.body() else []))])

#     def visitMctype(self,ctx:MCParser.MctypeContext):
#         if ctx.INTTYPE():
#             return IntType()
#         else:
#             return VoidType()

#     def visitBody(self,ctx:MCParser.BodyContext):
#         return self.visit(ctx.funcall())
  
  	
#     def visitFuncall(self,ctx:MCParser.FuncallContext):
#         return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

#     def visitExp(self,ctx:MCParser.ExpContext):
#         if (ctx.funcall()):
#             return self.visit(ctx.funcall())
#         else:
#             return IntLiteral(int(ctx.INTLIT().getText()))

# 1711502
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *


def fatten(lst):
    if lst:
        if (type(lst[0]) == type(list())):
            return lst[0] + fatten(lst[1:])
        else:
            return [lst[0]] + fatten(lst[1:])
    else:
        return []

class ASTGeneration(MCVisitor):
    # program : decl+ EOF ;
    def visitProgram(self,ctx:MCParser.ProgramContext):

        return Program(fatten([self.visit(decl) for decl in ctx.decl()]))


    # decl : var_decl | func_decl ; 
    def visitDecl(self, ctx:MCParser.DeclContext):
        if (ctx.var_decl()):
            return self.visit(ctx.var_decl())
        else:
            return self.visit(ctx.func_decl())


    # CHINH SUA 
    # var_decl : primary_type var (COMMA var)* SEMI ;  
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        return list(VarDecl(var.ID().getText(), self.visit(ctx.primary_type())) if (var.ID()) else 
                VarDecl(var.element().ID().getText(), ArrayType(int(var.element().INTLIT().getText()), self.visit(ctx.primary_type())))
                for var in ctx.var())



    # primary_type : BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
    def visitPrimary_type(self, ctx:MCParser.Primary_typeContext):
        if ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()
    
    
    # func_decl : mctype ID LB list_params RB block_stmt
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.list_params())
        returnType = self.visit(ctx.mctype())
        body = self.visit(ctx.block_stmt())
        func_decl = FuncDecl(name, param, returnType, body)
        return func_decl


    # mctype : primary_type | VOIDTYPE | output_ptr_type;
    def visitMctype(self, ctx:MCParser.MctypeContext):
        if ctx.VOIDTYPE():
            return VoidType()
        else:
            return self.visit(ctx.getChild(0))


    # output_ptr_type : primary_type LSB RSB;
    def visitOutput_ptr_type(self, ctx:MCParser.Output_ptr_typeContext):
        return ArrayPointerType(self.visit(ctx.primary_type()))


    # list_params : (param_decl (COMMA param_decl)*)?;
    def visitList_params(self, ctx:MCParser.List_paramsContext):
        return [self.visit(param) for param in ctx.param_decl()]


    # param_decl : primary_type ID | primary_type ID LSB RSB;
    def visitParam_decl(self, ctx:MCParser.Param_declContext):
        if (ctx.getChildCount() == 2):
            return VarDecl(ctx.ID().getText(), self.visit(ctx.primary_type()))
        else:
            return VarDecl(ctx.ID().getText(), ArrayPointerType(self.visit(ctx.primary_type())))
    

    # block_stmt : LP stmt_var_decl* RP;
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return Block(fatten([self.visit(stmt_var) for stmt_var in ctx.stmt_var_decl()])) 


    # stmt_var_decl : stmt | var_decl;
    def visitStmt_var_decl(self, ctx:MCParser.Stmt_var_declContext):
        if (ctx.stmt()):
            return self.visit(ctx.stmt())
        else:
            return self.visit(ctx.var_decl())


    # stmt : if_stmt | do_while_stmt | for_stmt | break_stmt | continue_stmt | return_stmt | expr_stmt | block_stmt;
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visit(ctx.getChild(0))


    # if_stmt : IF LB expr RB stmt (ELSE stmt)?;
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        if (ctx.ELSE()):
            expr = self.visit(ctx.expr())
            stmt0 = self.visit(ctx.stmt(0))
            stmt1 = self.visit(ctx.stmt(1))
            return If(expr, stmt0, stmt1)
        else:
            expr = self.visit(ctx.expr())
            stmt0 = self.visit(ctx.stmt(0))
            return If(expr, stmt0)


    # do_while_stmt : DO (stmt)+ WHILE expr SEMI; 
    def visitDo_while_stmt(self, ctx:MCParser.Do_while_stmtContext):
        lst_stmt = [self.visit(stmt) for stmt in ctx.stmt()]
        expr = self.visit(ctx.expr())
        return Dowhile(lst_stmt, expr)


    # for_stmt : FOR LB expr SEMI expr SEMI expr RB stmt;
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        expr0 = self.visit(ctx.expr(0))
        expr1 = self.visit(ctx.expr(1))
        expr2 = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        return For(expr0, expr1, expr2, stmt)


    # break_stmt : BREAK SEMI;
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return Break()


    # continue_stmt : CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return Continue()


    # return_stmt : RETURN expr? SEMI;
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        if (ctx.expr()):
            expr = self.visit(ctx.expr())
            return Return(expr)
        else:
            return Return()


    # expr_stmt : expr SEMI;   
    def visitExpr_stmt(self, ctx:MCParser.Expr_stmtContext):
        return self.visit(ctx.expr())


    # expr : expr1 ASSIGN_OP expr | expr1;
    def visitExpr(self, ctx:MCParser.ExprContext):
        if (ctx.getChildCount() == 3):
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr1())


    # expr1 : expr1 OR_OP expr2 | expr2;
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        if (ctx.getChildCount() == 3):
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr2())


    # expr2 : expr2 AND_OP expr3 | expr3;
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        if (ctx.getChildCount() == 3):
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.expr3())


    # expr3 : expr4 (EQUAL_OP | NOT_EQUAL_OP) expr4 | expr4;
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr4(0))
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr4(0))
            right = self.visit(ctx.expr4(1))
            return BinaryOp(op, left, right)


    # expr4 : expr5 (LESS_OP | LESS_EQUAL_OP | GREATER_EQUAL_OP | GREATER_OP) expr5 | expr5;
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr5(0))
        else:
            left = self.visit(ctx.expr5(0))
            right = self.visit(ctx.expr5(1))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)


    # expr5 : expr5 (ADD_OP | SUB_OP) expr6 | expr6;
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr6())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr5())
            right = self.visit(ctx.expr6())
            return BinaryOp(op, left, right)


    # expr6 : expr6 (DIV_OP | MUL_OP | MODULUS_OP) expr7 | expr7;
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr7())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr6())
            right = self.visit(ctx.expr7())
            return BinaryOp(op, left, right)


    # expr7 : (SUB_OP |NOT_OP) expr7 | expr8;
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr8())
        else:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.expr7())
            return UnaryOp(op, expr)


    # expr8 : expr9 LSB expr RSB | expr9;
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.expr9())
        else:
            arr = self.visit(ctx.expr9())
            idx = self.visit(ctx.expr())
            return ArrayCell(arr, idx)
    

    # expr9 : LB expr RB | call_func | lit | ID;
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        if (ctx.getChildCount() == 3):
            return self.visit(ctx.expr())
        else:
            if (ctx.call_func()):
                return self.visit(ctx.call_func())
            elif (ctx.lit()):
                return self.visit(ctx.lit())
            else:
                return Id(ctx.ID().getText())


    # call_func : ID LB list_exprs RB;
    def visitCall_func(self, ctx:MCParser.Call_funcContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.list_exprs())
        return CallExpr(method, param)


    # list_exprs : (expr (COMMA expr)*)?;
    def visitList_exprs(self, ctx:MCParser.List_exprsContext):
        return [self.visit(expr) for expr in ctx.expr()]


    # lit : INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
    def visitLit(self, ctx:MCParser.LitContext):
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif (ctx.BOOLLIT()):
            val = 1 if ctx.BOOLLIT().getText() == 'true' else 0
            return BooleanLiteral(bool(val))
        else:
            return StringLiteral(ctx.STRINGLIT().getText())


