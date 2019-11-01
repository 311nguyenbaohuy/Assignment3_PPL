
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

# from main.mc.utils.AST import *
# from main.mc.utils.Utils import *
# from main.mc.utils.Visitor import *
# from main.mc.checker.StaticError import *

from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class Checker:
    def __init__(self, global_scope, local_scope, returnType = None, id=True, do_while=True):
        self.global_scope = [*global_scope]
        self.local_scope = [*local_scope]
        self.returnType = returnType
        self.id = id
        self.do_while = do_while

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt", MType([],IntType())),
    Symbol("putInt", MType([IntType()], VoidType())),
    Symbol("putIntLn", MType([IntType()],VoidType())),
    Symbol("getFloat", MType([], FloatType())),
    Symbol("putFloat", MType([FloatType()], VoidType())),
    Symbol("putFloatLn", MType([FloatType()],VoidType())),
    Symbol("putBool", MType([BoolType()],VoidType())),
    Symbol("putBoolLn", MType([BoolType()],VoidType())),
    Symbol("putString", MType([StringType()],VoidType())),
    ]

    
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast
        self.func_invoke = []

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)


    def visitProgram(self,ast, c): 
        global_decls = [*c]
        entry_point = False
        lst_funcDecl = []
        
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                res = self.lookup(decl.variable, global_decls, lambda x: x.name)
                if res is None:
                    global_decls.append(Symbol(decl.variable, decl.varType))
                else:
                    raise Redeclared(Variable(), decl.variable)

            else:
                res = self.lookup(decl.name.name, global_decls, lambda x: x.name)
                if res is None:
                    lst_param = list(map(lambda var_decl: var_decl.varType, decl.param))
                    global_decls.append(Symbol(decl.name.name, MType(lst_param, decl.returnType)))
            
                    if decl.name.name == 'main' and len(decl.param) == 0 and type(decl.returnType) is VoidType:
                        entry_point = True
                    
                    lst_funcDecl.append(decl)
                    if decl.name.name != 'main':
                        self.func_invoke.append(decl.name.name)
                else:
                    raise Redeclared(Function(), decl.name.name)
        
        reduce(lambda x,y: x + [self.visit(y, x[0])], lst_funcDecl, [global_decls])
        if not entry_point:
            raise NoEntryPoint()
        if (self.func_invoke):
            raise UnreachableFunction(self.func_invoke[0])

    
    def visitFuncDecl(self, ast, c):
        # c is global variable/ function
        
        # local_decls = reduce(lambda x,y: x + [self.visit(y, (c, x))], ast.param, [])
        local_decls = reduce(lambda x,y: x + [self.visit(y, Checker(c, x, None, False))], ast.param, [])
        returnType = ast.returnType

        # return [ list(Symbol) ]
        # return self.visit(ast.body, (c, local_decls, returnType))
        returnStmt = type(self.visit(ast.body, Checker(c, local_decls, returnType))) is Return
        if not returnStmt:
            raise FunctionNotReturn(ast.name.name)
    
    def visitVarDecl(self, ast, c):
        # c[0] is global decls
        # c[1] is local decls

        # res = self.lookup(ast.variable, c[1], lambda x: x.name)
        res = self.lookup(ast.variable, c.local_scope, lambda x: x.name)
        if res is None:
            return Symbol(ast.variable, ast.varType)
        elif not c.id:
            raise Redeclared(Parameter(), ast.variable)
        else:
            raise Redeclared(Variable(), ast.variable)
    
    def visitBlock(self, ast, c):
        # return [ list(Symbol) ]
        stmtReturn = type(c.returnType) is VoidType
        blockReturn = False
        for x in ast.member:
            
            if isinstance(x, Block):
                blockReturn = type(self.visit(x, Checker(c.global_scope + c.local_scope, [], c.returnType))) is Return
            elif isinstance(x, VarDecl):
                c.local_scope.append(self.visit(x, c))
            else:
                
                stmtReturn = (type(self.visit(x, c)) is Return) or stmtReturn
                
                
        return Return(None) if (stmtReturn or blockReturn) else 0

    def visitBinaryOp(self, ast, c):
        LHS = self.visit(ast.left, c) 
        RHS = self.visit(ast.right, c) 

        if (ast.op == '='):
            if type(LHS) == type(RHS) and not isinstance(LHS, (VoidType, ArrayPointerType, ArrayType)):
                if type(ast.left) is Id or type(ast.left) is ArrayCell:
                    return type(LHS)
                else:
                    raise NotLeftValue(ast)
            elif type(LHS) == FloatType and type(RHS) == IntType:
                if type(ast.left) is Id or type(ast.left) is ArrayCell:
                    return type(LHS)
                else:
                    raise NotLeftValue(ast)
            else:
                raise TypeMismatchInExpression(ast)

        elif (ast.op == '||' or ast.op == '&&'):
            if type(LHS) == type(RHS) == BoolType:
                return type(LHS)
            else:
                raise TypeMismatchInExpression(ast)

        elif (ast.op == '==' or ast.op == '!='):
            if type(LHS) == type(RHS) and isinstance(LHS, (IntType, BoolType)):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif (ast.op == '%'):
            if type(LHS) == type(RHS) and type(LHS) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)

        elif (ast.op == '+' or ast.op == '-' or ast.op == '*' or ast.op == '/'):
            if type(LHS) == type(RHS) and type(LHS) is IntType:
                return IntType()
            elif type(LHS) == type(RHS) and type(LHS) is FloatType:
                return FloatType()
            elif type(LHS) is FloatType and type(RHS) is IntType:
                return FloatType()
            elif type(LHS) is IntType and type(RHS) is FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
                
        elif (ast.op == '>' or ast.op == '>=' or ast.op == '<' or ast.op == '<='):
            if type(LHS) == type(RHS) and type(LHS) is IntType:
                return BoolType()
            elif type(LHS) == type(RHS) and type(LHS) is FloatType:
                return BoolType()
            elif type(LHS) is FloatType and type(RHS) is IntType:
                return BoolType()
            elif type(LHS) is IntType and type(RHS) is FloatType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)        
        else:
            raise TypeMismatchInExpression(ast) 

    def visitUnaryOp(self, ast, c):
        exp = self.visit(ast.body, c) 
        if ast.op == '!' and type(exp) is BoolType:
            return BoolType()
        elif ast.op == '-' and isinstance(exp, (IntType, BoolType)):
            return exp
        else:
            raise TypeMismatchInExpression(ast) 

    def visitId(self, ast, c):

        res = self.lookup(ast.name, (c.global_scope + c.local_scope)[::-1], lambda x: x.name)
        if res is None:
            raise (Undeclared(Variable(), ast.name) if c.id else Undeclared(Parameter(), ast.name))
        else:
            return res.mtype
    
    def visitArrayCell(self, ast, c):
        # c[0] is list of global and local 
        # c[1] is False(Param) / True(ID)
        arrType = self.visit(ast.arr, c)
        idxType = self.visit(ast.idx, c)
        if not isinstance(arrType, (ArrayType, ArrayPointerType)) or not isinstance(idxType, IntType):
            raise TypeMismatchInExpression(ast)
        else:
            return arrType.eleType

    def visitCallExpr(self, ast, c): 

        at = [self.visit(x,Checker(c.global_scope, c.local_scope, c.returnType, False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,(c.global_scope)[::-1],lambda x: x.name)
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)
        else:
            lst = zip(res.mtype.partype, at)
            isOk = True
            for param in lst:
                isOk = isOk & ((type(param[0]) == type(param[1]) or (type(param[0]) is IntType and type(param[1]) is FloatType)))
            if isOk:
                if self.func_invoke:
                    self.func_invoke.remove(ast.method.name)
                return res.mtype.rettype
            else:
                raise TypeMismatchInExpression(ast)   

    def visitReturn(self, ast, c):
        if type(c.returnType) is VoidType and ast.expr is None:
            return Return(None)
        elif type(c.returnType) is VoidType and ast.expr is not None:
            raise TypeMismatchInStatement(ast)
        
        returnType = self.visit(ast.expr, c)

        if type(c.returnType) == type(returnType):
            return Return(None)
        elif type(c.returnType) is ArrayPointerType and type(returnType) is ArrayType:
            return Return(None)
        else:
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c):
        exprType = self.visit(ast.expr, c)
        if type(exprType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        returnIf = type(self.visit(ast.thenStmt, c)) is Return
        returnElse = False
        if ast.elseStmt is not None:
            returnElse = type(self.visit(ast.elseStmt, c)) is Return
        return Return(None) if returnIf and returnElse else 0

    def visitFor(self, ast, c):
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        expr3 = self.visit(ast.expr3, c)
        if type(expr1) is not IntType or type(expr2) is not BoolType or type(expr3) is not IntType:
            raise TypeMismatchInStatement(ast)
        hasReturn = type(self.visit(ast.loop, Checker(c.global_scope, c.local_scope, c.returnType, c.id, False))) is Return
        # return Return(None) if hasReturn else 0
        return 0

    def visitDowhile(self, ast, c):
        expr = self.visit(ast.exp, c)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        lst = [type(self.visit(x, Checker(c.global_scope, c.local_scope, c.returnType, c.id, False))) is Return for x in ast.sl]
        # return Renturn(None) if any(lst) else 0
        return 0

    def visitBreak(self, ast, c):
        if c.do_while:
            raise BreakNotInLoop()
        return Break()

    def visitContinue(self, ast, c):
        if c.do_while:
            raise ContinueNotInLoop()
        return Continue()

    def visitIntLiteral(self,ast, c): 
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()


     