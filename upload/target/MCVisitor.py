# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_decl.
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primary_type.
    def visitPrimary_type(self, ctx:MCParser.Primary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#element.
    def visitElement(self, ctx:MCParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_decl.
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#output_ptr_type.
    def visitOutput_ptr_type(self, ctx:MCParser.Output_ptr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_params.
    def visitList_params(self, ctx:MCParser.List_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param_decl.
    def visitParam_decl(self, ctx:MCParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#call_func.
    def visitCall_func(self, ctx:MCParser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_exprs.
    def visitList_exprs(self, ctx:MCParser.List_exprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MCParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_stmt.
    def visitExpr_stmt(self, ctx:MCParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt_var_decl.
    def visitStmt_var_decl(self, ctx:MCParser.Stmt_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr9.
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#lit.
    def visitLit(self, ctx:MCParser.LitContext):
        return self.visitChildren(ctx)



del MCParser