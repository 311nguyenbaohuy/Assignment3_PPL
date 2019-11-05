import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_decl_var_int(self):
        """
        int a;
        void main(){ return; }
        """
        input = Program([
                        VarDecl("a", IntType()),
                        FuncDecl(Id('main'),
                            [], 
                            VoidType(),
                            Block([
                                Return(None)
                            ]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_Decls_Int(self):
        """
        int a;
        int b;
        void main(){ return;}
        """
        input = Program([
                        VarDecl("a", IntType()),
                        VarDecl("b", IntType()),
                        FuncDecl(Id('main'),[], VoidType(),Block([Return(None)]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_ReDecl_var_int(self):
        """
        int a;
        float a;
        void main(){ return; }
        """
        input = Program([
                        VarDecl("a", IntType()),
                        VarDecl("a", FloatType()),
                        FuncDecl(Id('main'),[], VoidType(),Block([Return(None)]))
                        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_ReDecl_Float(self):
        """
        int a[5];
        float a;
        void main(){return;}
        """
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("a", FloatType()),
                        FuncDecl(Id('main'),[], VoidType(),Block([Return(None)]))
                        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_ReDecl_String(self):
        """
        int a[5];
        void main() {return;}
        """
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        FuncDecl(Id('main'),[], VoidType(),Block([Id('a')]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_Decl_Func(self):
        """
        int a[5];
        void foo() {}
        """
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        FuncDecl(Id('foo'),[], VoidType(),Block([])),
                        FuncDecl(Id('main'),[], VoidType(),Block([CallExpr(Id('foo'),[]), Return(None)]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_ReDecl_Func(self):

        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        FuncDecl(Id('main'),[], VoidType(),Block([Return(None)])),
                        FuncDecl(Id('main'),[], VoidType(),Block([Return(None)]))
                        ])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,406))


    def test_Decl_Param(self):

        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        FuncDecl(Id('foo'),[VarDecl("a", ArrayPointerType(IntType()))], VoidType(),Block([Return(None)])),
                        FuncDecl(Id('main'),[], VoidType(),Block([CallExpr(Id('foo'),[Id('a')]), Return(None)]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))


    def test_Decl_Param_Complex(self):

        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("b", IntType()),
                        FuncDecl(Id('foo'),[VarDecl("a", ArrayPointerType(IntType()))], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a')])
                                ])),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a')]), 
                                Return(None)
                                ]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_ReDecl_Param(self):

        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("b", ArrayType(5, IntType())),
                        FuncDecl(Id('foo'),
                            [VarDecl("a", ArrayPointerType(IntType())), VarDecl("a", ArrayPointerType(IntType()))], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a')])
                                ])),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a'), Id('b')]), 
                                Return(None)
                                ]))
                        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,409))


    def test_ReDecl_Param(self):

        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("b", ArrayType(5, IntType())),
                        FuncDecl(Id('foo'),
                            [VarDecl("a", ArrayPointerType(IntType())), VarDecl("a", ArrayPointerType(IntType()))], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a'), Id('a')])
                                ])),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a'), Id('b')]), 
                                Return(None)
                                ]))
                        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,409))


    def test_Complex_ReDecl_Param(self):
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("b", ArrayType(5, IntType())),
                        FuncDecl(Id('foo'),
                            [VarDecl("a", ArrayPointerType(IntType())), VarDecl("b", ArrayPointerType(IntType()))], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a'), Id('a')])
                                ])),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                CallExpr(Id('function'),[Id('a'), Id('b')]), 
                                Return(None)
                                ])),
                        FuncDecl(Id('function'),
                            [VarDecl("a", ArrayPointerType(IntType())), VarDecl("a", ArrayPointerType(IntType()))], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a')])
                                ]))
                        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,410)) 

    def test_ArrayCell(self):
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("b", ArrayType(5, IntType())),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                ArrayCell(Id('a'), IntLiteral('1'))
                                ]))
                        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,411)) 

    def test_Undecl_arr(self):
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        VarDecl("b", ArrayType(5, IntType())),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                ArrayCell(Id('c'), IntLiteral('1'))
                                ]))
                        ])
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,412)) 


    def test_Undecl_idx(self):
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                ArrayCell(Id('a'), Id('b'))
                                ]))
                        ])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,413)) 

    def test_Undecl_param(self):
        input = Program([
                        VarDecl("a", ArrayType(5, IntType())),
                        FuncDecl(Id('main'),[], 
                            VoidType(),
                            Block([
                                ArrayCell(Id('a'), Id('b'))
                                ])),
                        FuncDecl(Id('foo'),
                            [VarDecl("a", ArrayPointerType(IntType())), VarDecl("b", ArrayPointerType(IntType()))], 
                            VoidType(),
                            Block([
                                CallExpr(Id('foo'),[Id('a'), Id('b')])
                                ]))
                        ])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,414)) 


    def test_Undeclared_Recursise_func(self):
        """
        int foo(){
            return foo();
        }
        void main(){
            int foo;
            foo();
        }
        """
        input = Program([
                    FuncDecl(Id('foo'),[],IntType(),
                        Block([Return(CallExpr(Id('foo'),[]))])),
                    FuncDecl(Id('main'),[],VoidType(),
                        Block([VarDecl('foo',IntType()),CallExpr(Id('foo'),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,415)) 


    def test_Recursise_func(self):
        """
        int foo(){
            return foo();
        }
        void main(){
            foo();
        }
        """
        input = Program([
                FuncDecl(Id('foo'),[],IntType(),
                    Block([Return(CallExpr(Id('foo'),[]))])),
                FuncDecl(Id('main'),[],VoidType(),
                    Block([CallExpr(Id('foo'),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416)) 

    def test_Array(self):
        """
        int a[5];
        void main(){
            a[5]; 
        }
        """
        input = Program([
                VarDecl('a',ArrayType(5,IntType())),
                FuncDecl(Id('main'),[],VoidType(),
                    Block([ArrayCell(Id('a'),IntLiteral(5))]))
                ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417)) 

    def test_Array_missMatch(self):
        """
        int a[5];
        void main(){
            a[a]; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,IntType())),FuncDecl(Id('main'),[],VoidType(),Block([ArrayCell(Id('a'),Id('a'))]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,418)) 

    def test_binOp_int_int(self):
        """
        int a[5];
        int b;
        void main(){
            a[b] + b; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,IntType())),VarDecl('b',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('+',ArrayCell(Id('a'),Id('b')),Id('b'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,419)) 

    def test_binOp_int_intlit(self):
        """
        int a[5];
        int b;
        void main(){
            a[b] + 1; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,IntType())),VarDecl('b',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('+',ArrayCell(Id('a'),Id('b')),IntLiteral(1))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420)) 

    def test_binOp_String_Stringlit(self):
        """
        string a[5];
        int b;
        void main(){
            a[b] + "abc"; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,StringType())),VarDecl('b',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('+',ArrayCell(Id('a'),Id('b')),StringLiteral('abc'))]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(a),Id(b)),StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_binOp_Boolean(self):
        """
        boolean a[5];
        int b;
        void main(){
            a[b-1] = a[b] || a[1]; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,BoolType())),VarDecl('b',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',ArrayCell(Id('a'),BinaryOp('-',Id('b'),IntLiteral(1))),BinaryOp('||',ArrayCell(Id('a'),Id('b')),ArrayCell(Id('a'),IntLiteral(1))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422)) 

    def test_binOp_Boolean_function(self):
        """
        boolean a[5];
        int b;
        boolean[] foo(){
            return a;
        }
        void main(){
            a[b-1] = a[b] != foo()[b]; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,BoolType())),VarDecl('b',IntType()),FuncDecl(Id('foo'),[],ArrayPointerType(BoolType()),Block([Return(Id('a'))])),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',ArrayCell(Id('a'),BinaryOp('-',Id('b'),IntLiteral(1))),BinaryOp('!=',ArrayCell(Id('a'),Id('b')),ArrayCell(CallExpr(Id('foo'),[]),Id('b'))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,423)) 

    def test_binOp_Boolean_function_(self):
        """
        boolean a[5];
        int b;
        boolean[] foo(){
            return a;
        }
        void main(){
            a[b-1] = !(a[b] == foo()[b]); 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,BoolType())),VarDecl('b',IntType()),FuncDecl(Id('foo'),[],ArrayPointerType(BoolType()),Block([Return(Id('a'))])),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',ArrayCell(Id('a'),BinaryOp('-',Id('b'),IntLiteral(1))),UnaryOp('!',BinaryOp('==',ArrayCell(Id('a'),Id('b')),ArrayCell(CallExpr(Id('foo'),[]),Id('b')))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,424)) 

    def test_binOp_BooleanArray_with_sub(self):
        """
        boolean a[5];
        int b;
        boolean[] foo(int b){
            return a;
        }
        void main(){
            a[b-1] = -foo(b)[b]; 
        }
        """
        input = Program([VarDecl('a',ArrayType(5,BoolType())),VarDecl('b',IntType()),FuncDecl(Id('foo'),[VarDecl('b',IntType())],ArrayPointerType(BoolType()),Block([Return(Id('a'))])),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',ArrayCell(Id('a'),BinaryOp('-',Id('b'),IntLiteral(1))),UnaryOp('-',ArrayCell(CallExpr(Id('foo'),[Id('b')]),Id('b'))))]))])
        expect = "Type Mismatch In Expression: UnaryOp(-,ArrayCell(CallExpr(Id(foo),[Id(b)]),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,425)) 

    def test_binOp_Float_int(self):
        """
        int b;
        float a;
        void main(){
            a = b; 
        }
        """
        input = Program([VarDecl('b',IntType()),VarDecl('a',FloatType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',Id('a'),Id('b'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,426)) 

    def test_Assign_Float_int(self):
        """
        int b;
        float a;
        void main(){
            a = b + a + 1.0; 
        }
        """
        input = Program([VarDecl('b',IntType()),VarDecl('a',FloatType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('+',Id('b'),Id('a')),FloatLiteral(1.0)))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427)) 


    def test_Assign_Float_Expr(self):
        """
        int b;
        float a;
        void main(){
            a = (b + a * 2+ 1.0) / 2; 
        }
        """
        input = Program([VarDecl('b',IntType()),VarDecl('a',FloatType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',Id('a'),BinaryOp('/',BinaryOp('+',BinaryOp('+',Id('b'),BinaryOp('*',Id('a'),IntLiteral(2))),FloatLiteral(1.0)),IntLiteral(2)))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428)) 

    def test_Assign_Float_Func(self):
        """
        float foo(){
            return 1.0;
        }
        float func1(float a){
            return foo();
        }
        void main(){
            float b[2]; 
            b[1] = func1(foo());
        }
        """
        input = Program([FuncDecl(Id('foo'),[],FloatType(),Block([Return(FloatLiteral(1.0))])),FuncDecl(Id('func1'),[VarDecl('a',FloatType())],FloatType(),Block([Return(CallExpr(Id('foo'),[]))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',ArrayType(2,FloatType())),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),CallExpr(Id('func1'),[CallExpr(Id('foo'),[])]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429)) 

    def test_Float_Assign_Func_with_Int_param(self):
        """
        int[] func1(float a){
            int c[4];
            return c;
        }
        void main(){
            float b[2]; 
            b[1] = func1(b[1])[1];
        }
        """
        input = Program([FuncDecl(Id('func1'),[VarDecl('a',FloatType())],ArrayPointerType(IntType()),Block([VarDecl('c',ArrayType(4,IntType())),Return(Id('c'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',ArrayType(2,FloatType())),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),ArrayCell(CallExpr(Id('func1'),[ArrayCell(Id('b'),IntLiteral(1))]),IntLiteral(1)))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_Float_Assign_Func_with_Int_param(self):
        """
        int[] func1(float a){
            int c[4];
            return c;
        }
        void main(){
            float b[2]; 
            b[1] = func1(b[1])[1];
        }
        """
        input = Program([FuncDecl(Id('func1'),[VarDecl('a',FloatType())],ArrayPointerType(IntType()),Block([VarDecl('c',ArrayType(4,IntType())),Return(Id('c'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',ArrayType(2,FloatType())),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),ArrayCell(CallExpr(Id('func1'),[ArrayCell(Id('b'),IntLiteral(1))]),IntLiteral(1)))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_Float_Assign_Func_with_Int_param(self):
        """
        int[] func1(float a){
            int c[4];
            return c;
        }
        void main(){
            float b[2]; 
            b[1] = func1(b[1])[1];
        }
        """
        input = Program([FuncDecl(Id('func1'),[VarDecl('a',FloatType())],ArrayPointerType(IntType()),Block([VarDecl('c',ArrayType(4,IntType())),Return(Id('c'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',ArrayType(2,FloatType())),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),ArrayCell(CallExpr(Id('func1'),[ArrayCell(Id('b'),IntLiteral(1))]),IntLiteral(1)))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_Int_Assign_Float(self):
        """
        void main(){
            int a;
            float b;
            a = b;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',FloatType()),BinaryOp('=',Id('a'),Id('b'))]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_CompareIntFloat(self):
        """
        boolean[] foo(float a){
            boolean b[3];
            return b;
        }
        void main(){
            int a;
            float b;
            foo(b)[1] = b > a;
        }
        """
        input = Program([FuncDecl(Id('foo'),[VarDecl('a',FloatType())],ArrayPointerType(BoolType()),Block([VarDecl('b',ArrayType(3,BoolType())),Return(Id('b'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',FloatType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[Id('b')]),IntLiteral(1)),BinaryOp('>',Id('b'),Id('a')))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_CompareIntBoolean(self):
        """
        boolean[] foo(float a){
            boolean b[3];
            return b;
        }
        void main(){
            int a;
            float b;
            foo(b)[1] = b > foo(b)[a];
        }
        """
        input = Program([FuncDecl(Id('foo'),[VarDecl('a',FloatType())],ArrayPointerType(BoolType()),Block([VarDecl('b',ArrayType(3,BoolType())),Return(Id('b'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',FloatType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[Id('b')]),IntLiteral(1)),BinaryOp('>',Id('b'),ArrayCell(CallExpr(Id('foo'),[Id('b')]),Id('a'))))]))])
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(b),ArrayCell(CallExpr(Id(foo),[Id(b)]),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_StringAssign(self):
        """
        string foo(){
            return "abc";
        }
        void main(){
            string a;
            a = foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',StringType()),BinaryOp('=',Id('a'),CallExpr(Id('foo'),[]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_UnaryOPStringAssign(self):
        """
        string foo(){
            return "abc";
        }
        void main(){
            string a;
            a = !foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',StringType()),BinaryOp('=',Id('a'),UnaryOp('!',CallExpr(Id('foo'),[])))]))])
        expect = "Type Mismatch In Expression: UnaryOp(!,CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_FuncCall(self):
        """
        string foo(int a, float b[]){
            return "abc";
        }
        void main(){
            string b;
            int a[2];
            b = foo(a[1], a);
        }
        """
        input = Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(FloatType()))],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',StringType()),VarDecl('a',ArrayType(2,IntType())),BinaryOp('=',Id('b'),CallExpr(Id('foo'),[ArrayCell(Id('a'),IntLiteral(1)),Id('a')]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_FuncCall_Not_enough_params(self):
        """
        string foo(int a, float b[]){
            return "abc";
        }
        void main(){
            string b;
            int a[2];
            b = foo(a[1]);
        }
        """
        input = Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(FloatType()))],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',StringType()),VarDecl('a',ArrayType(2,IntType())),BinaryOp('=',Id('b'),CallExpr(Id('foo'),[ArrayCell(Id('a'),IntLiteral(1))]))]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_FuncCall_Not_enough_params(self):
        """
        string foo(int a, float b[]){
            return "abc";
        }
        void main(){
            string b;
            int a[2];
            b = foo(a[1]);
        }
        """
        input = Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(FloatType()))],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',StringType()),VarDecl('a',ArrayType(2,IntType())),BinaryOp('=',Id('b'),CallExpr(Id('foo'),[ArrayCell(Id('a'),IntLiteral(1))]))]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_Func_param(self):
        """
        int foo1(){
            return 1*2;
        }
        int foo2(){
            return 1%2;
        }
        string foo3(int a, int b){
            return "abc";
        }
        void main(){
            string b;
            b = foo3(foo1(), foo2());
        }
        """
        input = Program([FuncDecl(Id('foo1'),[],IntType(),Block([Return(BinaryOp('*',IntLiteral(1),IntLiteral(2)))])),FuncDecl(Id('foo2'),[],IntType(),Block([Return(BinaryOp('%',IntLiteral(1),IntLiteral(2)))])),FuncDecl(Id('foo3'),[VarDecl('a',IntType()),VarDecl('b',IntType())],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',StringType()),BinaryOp('=',Id('b'),CallExpr(Id('foo3'),[CallExpr(Id('foo1'),[]),CallExpr(Id('foo2'),[])]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_ArrayFunc_param(self):
        """
        int[] foo1(){
            int a[3];
            return a;
        }
        int[] foo2(){
            int a[3];
            return a;
        }
        string foo3(int a[], int b[]){
            return "abc";
        }
        void main(){
            string b;
            b = foo3(foo1(), foo2());
        }
        """
        input = Program([FuncDecl(Id('foo1'),[],ArrayPointerType(IntType()),Block([VarDecl('a',ArrayType(3,IntType())),Return(Id('a'))])),FuncDecl(Id('foo2'),[],ArrayPointerType(IntType()),Block([VarDecl('a',ArrayType(3,IntType())),Return(Id('a'))])),FuncDecl(Id('foo3'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('b',ArrayPointerType(IntType()))],StringType(),Block([Return(StringLiteral('abc'))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('b',StringType()),BinaryOp('=',Id('b'),CallExpr(Id('foo3'),[CallExpr(Id('foo1'),[]),CallExpr(Id('foo2'),[])]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))
    

    def test_IfElse_stmt(self):
        """
        void main(){
            int a;
            a = 11 * 2;
            if (a > 1){
                getInt();
            }
            else{
                putInt(1);
            }
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('*',IntLiteral(11),IntLiteral(2))),If(BinaryOp('>',Id('a'),IntLiteral(1)),Block([CallExpr(Id('getInt'),[])]),Block([CallExpr(Id('putInt'),[IntLiteral(1)])]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))


    def test_If_stmt(self):
        """
        void main(){
            int a;
            a = 11 * 2;
            if (a > 1)
                getInt();
            
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('*',IntLiteral(11),IntLiteral(2))),If(BinaryOp('>',Id('a'),IntLiteral(1)),CallExpr(Id('getInt'),[]),None)]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))


    def test_If_stmt_cond(self):
        """
        void main(){
            int a;
            a = 11 * 2;
            if ((a > 1) && (a < 1) || !(a == 2))
                getInt();
            
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('*',IntLiteral(11),IntLiteral(2))),If(BinaryOp('||',BinaryOp('&&',BinaryOp('>',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),IntLiteral(1))),UnaryOp('!',BinaryOp('==',Id('a'),IntLiteral(2)))),CallExpr(Id('getInt'),[]),None)]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_If_stmt_wrongCond(self):
        """
        void main(){
            int a;
            a = 11 * 2;
            if (1/2 + 1 * 4 % 3)
                getInt();
            
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('*',IntLiteral(11),IntLiteral(2))),If(BinaryOp('+',BinaryOp('/',IntLiteral(1),IntLiteral(2)),BinaryOp('%',BinaryOp('*',IntLiteral(1),IntLiteral(4)),IntLiteral(3))),CallExpr(Id('getInt'),[]),None)]))])
        expect = "Type Mismatch In Statement: If(BinaryOp(+,BinaryOp(/,IntLiteral(1),IntLiteral(2)),BinaryOp(%,BinaryOp(*,IntLiteral(1),IntLiteral(4)),IntLiteral(3))),CallExpr(Id(getInt),[]))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_If_stmt_BoolCond(self):
        """
        void main(){
            boolean a;
            if (a = true)
                getInt();
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',BoolType()),If(BinaryOp('=',Id('a'),BooleanLiteral(True)),CallExpr(Id('getInt'),[]),None)]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_If_stmt_BoolCond(self):
        """
        void main(){
            boolean a;
            if (a = true)
                getInt();
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',BoolType()),If(BinaryOp('=',Id('a'),BooleanLiteral(True)),CallExpr(Id('getInt'),[]),None)]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_For_stmt(self):
        """
        void main(){
            for (1;false;1){ }
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),BooleanLiteral(False),IntLiteral(1),Block([]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_For_stmt_cond1(self):
        """
        void main(){
            for (1.2/3;false;1){ }
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([For(BinaryOp('/',FloatLiteral(1.2),IntLiteral(3)),BooleanLiteral(False),IntLiteral(1),Block([]))]))])
        expect = "Type Mismatch In Statement: For(BinaryOp(/,FloatLiteral(1.2),IntLiteral(3));BooleanLiteral(false);IntLiteral(1);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_For_stmt_cond2(self):
        """
        void main(){
            int a;
            for (a = 1 * 4 % 3; a - 1.2;  a = a + 1){ 
                return;
            }
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),BinaryOp('%',BinaryOp('*',IntLiteral(1),IntLiteral(4)),IntLiteral(3))),BinaryOp('-',Id('a'),FloatLiteral(1.2)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Block([Return(None)]))]))])
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),BinaryOp(%,BinaryOp(*,IntLiteral(1),IntLiteral(4)),IntLiteral(3)));BinaryOp(-,Id(a),FloatLiteral(1.2));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_For_stmt_cond3(self):
        """
        void main(){
            int a;
            for (a = 1 * 4 % 3; a - 1.2;  a + 1.2){ 
                return;
            }
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),BinaryOp('%',BinaryOp('*',IntLiteral(1),IntLiteral(4)),IntLiteral(3))),BinaryOp('==',Id('a'),IntLiteral(1)),BinaryOp('+',Id('a'),FloatLiteral(1.2)),Block([Return(None)]))]))])
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),BinaryOp(%,BinaryOp(*,IntLiteral(1),IntLiteral(4)),IntLiteral(3)));BinaryOp(==,Id(a),IntLiteral(1));BinaryOp(+,Id(a),FloatLiteral(1.2));Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_DoWhile(self):
        """
        void main(){
            int a;
            do{

            }
            {
                break;
            }
            while(true);
            
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([]),Block([Break()])],BooleanLiteral(True))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_DoWhileFor(self):
        """
        void main(){
            int a;
            do{
                int a;
                for (a = 1; a != 1; a + 1){
                    a == 1;
                }
            }
            while(true);
            
        }
        """
        input =Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('!=',Id('a'),IntLiteral(1)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([BinaryOp('==',Id('a'),IntLiteral(1))]))])],BooleanLiteral(True))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_DoWhileForDeclare(self):
        """
        void main(){
            int a;
            do{
                int a;
                for (a = 1; a != 1; a + 1){
                    int a;
                }
            }
            while(true);
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('!=',Id('a'),IntLiteral(1)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([VarDecl('a',IntType())]))])],BooleanLiteral(True))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_If_expec(self):
        """
        void main(){
            int a;
            do{
                int a;
                for (a = 1; a != 1; a + 1){
                    int a;
                }
                if (a > 0){
                    int a;
                }
            }
            while(true);
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('!=',Id('a'),IntLiteral(1)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([VarDecl('a',IntType())])),If(BinaryOp('>',Id('a'),IntLiteral(0)),Block([VarDecl('a',IntType())]),None)])],BooleanLiteral(True))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_Else_expec(self):
        """
        void main(){
            int a;
            do{
                int a;
                for (a = 1; a != 1; a + 1){
                    int a;
                }
                if (a > 0){
                    int a;
                }
                else{
                    int a;
                }
            }
            while(true);
            
        }
        """
        input =  Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),Dowhile([Block([VarDecl('a',IntType()),For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('!=',Id('a'),IntLiteral(1)),BinaryOp('+',Id('a'),IntLiteral(1)),Block([VarDecl('a',IntType())])),If(BinaryOp('>',Id('a'),IntLiteral(0)),Block([VarDecl('a',IntType())]),Block([VarDecl('a',IntType())]))])],BooleanLiteral(True))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))


    def test_Else_redeclare(self):
        """
        void main(){
            int a;
            if (a > 0){int a;}
            else {int a;}
            
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),If(BinaryOp('>',Id('a'),IntLiteral(0)),Block([VarDecl('a',IntType())]),Block([VarDecl('a',IntType())]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))

    
    def test_IntFunc_Return_boolean(self):
        """
        void main(){
            int a;
            foo();
            
        }
        int foo(){
            return true != false;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],IntType(),Block([Return(BinaryOp('!=',BooleanLiteral(True),BooleanLiteral(False)))]))])
        expect = "Type Mismatch In Statement: Return(BinaryOp(!=,BooleanLiteral(true),BooleanLiteral(false)))"
        self.assertTrue(TestChecker.test(input,expect,455))


    def test_FloatFunc_Return_Int(self):
        """
        void main(){
            int a;
            foo();
            
        }
        float foo(){
            return 1;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],FloatType(),Block([Return(IntLiteral(1))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))


    def test_FloatPointerFunc_Return_IntArray(self):
        """
        void main(){
            int a;
            foo();
            
        }
        float [] foo(){
            int a [4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],ArrayPointerType(FloatType()),Block([VarDecl('a',ArrayType(4,IntType())),Return(Id('a'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))


    def test_VoidFunc_Return_Int(self):
        """
        void main(){
            int a;
            foo();
            
        }
        void foo(){
            int a [4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],VoidType(),Block([VarDecl('a',ArrayType(4,IntType())),Return(Id('a'))]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,458))


    def test_OnlyBlockReturn(self):
        """
        void main(){
            int a;
            foo();
            
        }
        int foo(){
            int a [4];
            {return a[1];}
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('a',ArrayType(4,IntType())),Block([Return(ArrayCell(Id('a'),IntLiteral(1)))])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_MultiBlockReturn(self):
        """
        void main(){
            int a;
            foo();
            
        }
        int foo(){
            int a [4];
            {{{return a[1];}}}
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('a',ArrayType(4,IntType())),Block([Block([Block([Return(ArrayCell(Id('a'),IntLiteral(1)))])])])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_MultiBlock(self):
        """
        void main(){
            int a;
            foo();
            
        }
        int foo(){
            int a [4];
            {
                {int a;}
                {return a[1];}
                {int a[2];}
            }
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo'),[])])),FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('a',ArrayType(4,IntType())),Block([Block([VarDecl('a',IntType())]),Block([Return(ArrayCell(Id('a'),IntLiteral(1)))]),Block([VarDecl('a',ArrayType(2,IntType()))])])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_FloatArray_Return_IntArray(self):
        """
        void main(){
            int a;
            foo2();
        }
        int[] foo1(){
            int a [4];
            return a;
        }
        float[] foo2(){
            return foo1();
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo2'),[])])),FuncDecl(Id('foo1'),[],ArrayPointerType(IntType()),Block([VarDecl('a',ArrayType(4,IntType())),Return(Id('a'))])),FuncDecl(Id('foo2'),[],ArrayPointerType(FloatType()),Block([Return(CallExpr(Id('foo1'),[]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_Return_Bool_Expr(self):
        """
        void main(){
            int a;
            foo1();
        }
        boolean foo1(){
            return true == !false;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),CallExpr(Id('foo1'),[])])),FuncDecl(Id('foo1'),[],BoolType(),Block([Return(BinaryOp('==',BooleanLiteral(True),UnaryOp('!',BooleanLiteral(False))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_Break_in_doWhile(self):
        """
        void main(){
            do break;
            while(true != (false == true))
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([Break()])],BinaryOp('!=',BooleanLiteral(True),BinaryOp('==',BooleanLiteral(False),BooleanLiteral(True))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_Break_in_doWhile(self):
        """
        void main(){
            do {}{}{{break;}}
            while(true != (false == true))
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([]),Block([]),Block([Block([Break()])])],BinaryOp('!=',BooleanLiteral(True),BinaryOp('==',BooleanLiteral(False),BooleanLiteral(True))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_Break_in_doWhile_with_If(self):
        """
        void main(){
            do {
                if (true) break;
            }
            while(true != (false == true))
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([If(BooleanLiteral(True),Break(),None)])],BinaryOp('!=',BooleanLiteral(True),BinaryOp('==',BooleanLiteral(False),BooleanLiteral(True))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_Break_in_main(self):
        """
        void main(){
            break;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([Break()]))])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_Continue_in_For(self):
        """
        void main(){
            int i;
            for (i = 1; i < 10; i = i + 1){
                continue;
                break;
            }
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([Continue(),Break()]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))


    def test_Continue_in_If(self):
        """
        void main() {
            do{ 
                int i;
            } 
            while(i<1); 
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([VarDecl('i',IntType())])],BinaryOp('<',Id('i'),IntLiteral(1)))]))])
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_LHS_not_leftValue(self):
        """
        void main() {
            int i;
            i + 1 = i + 1; 
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),BinaryOp('=',BinaryOp('+',Id('i'),IntLiteral(1)),BinaryOp('+',Id('i'),IntLiteral(1)))]))])
        expect = "Not Left Value: BinaryOp(=,BinaryOp(+,Id(i),IntLiteral(1)),BinaryOp(+,Id(i),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_LHS_Multi_Assignment(self):
        """
        void main() {
            int i;
            int a;
            i = i  = a = a/2 + i % 4 * 3 -2; 
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),VarDecl('a',IntType()),BinaryOp('=',Id('i'),BinaryOp('=',Id('i'),BinaryOp('=',Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',BinaryOp('%',Id('i'),IntLiteral(4)),IntLiteral(3))),IntLiteral(2)))))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_FloatPointerFunc(self):
        """
        void main() {
            int i;
            int a;
            foo()[2] = a/2 + i % 4 * 3 -2; 
        }
        float[] foo(){
            float a[4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),VarDecl('a',IntType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(2)),BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',BinaryOp('%',Id('i'),IntLiteral(4)),IntLiteral(3))),IntLiteral(2)))])),FuncDecl(Id('foo'),[],ArrayPointerType(FloatType()),Block([VarDecl('a',ArrayType(4,FloatType())),Return(Id('a'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_FloatPointerFunc(self):
        """
        void main() {
            int i;
            int a;
            foo()[2] = a/2 + i % 4 * 3 -2; 
        }
        float[] foo(){
            float a[4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),VarDecl('a',IntType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(2)),BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',BinaryOp('%',Id('i'),IntLiteral(4)),IntLiteral(3))),IntLiteral(2)))])),FuncDecl(Id('foo'),[],ArrayPointerType(FloatType()),Block([VarDecl('a',ArrayType(4,FloatType())),Return(Id('a'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_No_entry_point(self):
        """
        int main() {
            int i;
            int a;
            foo()[2] = a/2 + i % 4 * 3 -2; 
            return a;
        }
        float[] foo(){
            float a[4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),VarDecl('a',IntType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(2)),BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',BinaryOp('%',Id('i'),IntLiteral(4)),IntLiteral(3))),IntLiteral(2))),Return(Id('a'))])),FuncDecl(Id('foo'),[],ArrayPointerType(FloatType()),Block([VarDecl('a',ArrayType(4,FloatType())),Return(Id('a'))]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_Recurise_main(self):
        """
        void main() {
            int i;
            int a;
            foo()[2] = a/2 + i % 4 * 3 -2; 
            main();
        }
        float[] foo(){
            float a[4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),VarDecl('a',IntType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(2)),BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',BinaryOp('%',Id('i'),IntLiteral(4)),IntLiteral(3))),IntLiteral(2))),CallExpr(Id('main'),[])])),FuncDecl(Id('foo'),[],ArrayPointerType(FloatType()),Block([VarDecl('a',ArrayType(4,FloatType())),Return(Id('a'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))


    def test_Recurise_main(self):
        """
        void main() {
            int i;
            int a;
            foo()[2] = a/2 + i % 4 * 3 -2; 
            main();
        }
        float[] foo(){
            float a[4];
            return a;
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('i',IntType()),VarDecl('a',IntType()),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(2)),BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',BinaryOp('%',Id('i'),IntLiteral(4)),IntLiteral(3))),IntLiteral(2))),CallExpr(Id('main'),[])])),FuncDecl(Id('foo'),[],ArrayPointerType(FloatType()),Block([VarDecl('a',ArrayType(4,FloatType())),Return(Id('a'))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))


    def test_VoidReturn(self):
        """
        void main() {
            if (true){

            }
            else{

            }
        }
        """
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([If(BooleanLiteral(True),Block([]),Block([]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_IntReturn(self):
        """
        int foo(){
            if (true) return 1;
            else return 0;
        }
        void main() {
            if (true){
                foo();
            }
            else{

            }
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([If(BooleanLiteral(True),Return(IntLiteral(1)),Return(IntLiteral(0)))])),FuncDecl(Id('main'),[],VoidType(),Block([If(BooleanLiteral(True),Block([CallExpr(Id('foo'),[])]),Block([]))]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_Else_Return_wrong(self):
        """
        int foo(){
            if (true){ 
                if (true){
                    return 1;
                }
                else{
                    return false;
                }
            }
            else{
                return 1;
            }
            
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BooleanLiteral(True),Block([Return(IntLiteral(1))]),Block([Return(BooleanLiteral(False))]))]),Block([Return(IntLiteral(1))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_Else_Return(self):
        """
        int foo(){
            if (true){ 
                if (true){
                    return 1;
                }
                else{
                    return 0;
                }
            }
            else{
                return 1;
            }
            
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BooleanLiteral(True),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(0))]))]),Block([Return(IntLiteral(1))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_Else_Not_Return(self):
        """
        int foo(){
            if (true){ 
                if (true){
                    return 1;
                }
            }
            else{
                return 1;
            }
            
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BooleanLiteral(True),Block([Return(IntLiteral(1))]),None)]),Block([Return(IntLiteral(1))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,478))


    def test_Else_Not_Return(self):
        """
        int foo(){
            if (true){ 
                if (true){
                    return 1;
                }
            }
            else{
                return 1;
            }
            
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BooleanLiteral(True),Block([Return(IntLiteral(1))]),None)]),Block([Return(IntLiteral(1))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_Foo_Not_Return(self):
        """
        int foo(){
            int i;
            for (i; i == 1; i){
                return 1;
            }
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('==',Id('i'),IntLiteral(1)),Id('i'),Block([Return(IntLiteral(1))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,479))


    def test_Foo_Not_Return_with_IfElse(self):
        """
        int foo(){
            int i;
            for (i; i == 1; i){
                if (true) return 1;
                else return 1;
            }
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('==',Id('i'),IntLiteral(1)),Id('i'),Block([If(BooleanLiteral(True),Return(IntLiteral(1)),Return(IntLiteral(1)))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_Foo_DoWhileReturn(self):
        """
        int foo(){
            int i;
            do{
                int i;
                i = 1;
                return i;
            } while(i < 1);
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),Dowhile([Block([VarDecl('i',IntType()),BinaryOp('=',Id('i'),IntLiteral(1)),Return(Id('i'))])],BinaryOp('<',Id('i'),IntLiteral(1)))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_Foo_DoWhile_Return_outside(self):
        """
        int foo(){
            int i;
            do{
                int i;
                i = 1;
                return i;
            } while(i < 1);
            return i;
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),Dowhile([Block([VarDecl('i',IntType()),BinaryOp('=',Id('i'),IntLiteral(1)),Return(Id('i'))])],BinaryOp('<',Id('i'),IntLiteral(1))),Return(Id('i'))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))


    def test_Foo_DoWhile_Return(self):
        """
        int foo(){
            int i;
            do{
                int i;
                i = 1;
                return i;
            } while(i < 1);
            return i;
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),Dowhile([Block([VarDecl('i',IntType()),BinaryOp('=',Id('i'),IntLiteral(1)),Return(Id('i'))])],BinaryOp('<',Id('i'),IntLiteral(1))),Return(Id('i'))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_Foo_DoWhile_IfElse_return_inside(self):
        """
        int foo(){
            int i;
            do{
                if (true) return 1;
                else return 0;
            } while(i < 1);
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),Dowhile([Block([If(BooleanLiteral(True),Return(IntLiteral(1)),Return(IntLiteral(0)))])],BinaryOp('<',Id('i'),IntLiteral(1)))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_Foo_DoWhile_IfElse_return_bothside(self):
        """
        int foo(){
            int i;
            do{
                if (true) return 1;
                else return 0;
            } while(i < 1);
            return i;
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),Dowhile([Block([If(BooleanLiteral(True),Return(IntLiteral(1)),Return(IntLiteral(0)))])],BinaryOp('<',Id('i'),IntLiteral(1))),Return(Id('i'))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_Foo_DoWhile_IfElse_return_bothside(self):
        """
        int foo(){
            int i;
            do{
                if (true) return 1;
                else return 0;
            } while(i < 1);
            return i;
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('i',IntType()),Dowhile([Block([If(BooleanLiteral(True),Return(IntLiteral(1)),Return(IntLiteral(0)))])],BinaryOp('<',Id('i'),IntLiteral(1))),Return(Id('i'))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_FooFunction_DoWhile_IfElse(self):
        """
        int foo(){
            int a;
            boolean b[2];
            if (b[a]) return a;
            else{
                do{
                    return a;
                }
                while(a == 1);
            }
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',ArrayType(2,BoolType())),If(ArrayCell(Id('b'),Id('a')),Return(Id('a')),Block([Dowhile([Block([Return(Id('a'))])],BinaryOp('==',Id('a'),IntLiteral(1)))]))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,486))


    def test_FooFunction_while_expr(self):
        """
        int foo(){
            int a;
            boolean b;
            do{
                return a;
            }
            while(b = a + 1 == a /2);
        }
        void main() {
            foo();
        }
        """
        input = Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',BoolType()),Dowhile([Block([Return(Id('a'))])],BinaryOp('=',Id('b'),BinaryOp('==',BinaryOp('+',Id('a'),IntLiteral(1)),BinaryOp('/',Id('a'),IntLiteral(2)))))])),FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))
