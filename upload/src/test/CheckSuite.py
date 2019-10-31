import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_int_varDecl(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),
    #                         [], 
    #                         VoidType(),
    #                         Block([
    #                             BinaryOp('+',Id('a'),Id('a'))
    #                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_More_int_VarDecl(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     VarDecl("b", IntType()),
    #                     FuncDecl(Id('main'),[], VoidType(),Block([Return()]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_int_ReVarDecl(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[], VoidType(),Block([Return()]))
    #                     ])
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    

    # def test_main_ReFuncDecl(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[], VoidType(),Block([Return()])),
    #                     FuncDecl(Id('main'),[], VoidType(),Block([Return()]))
    #                     ])
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    

    # def test_main_FuncDecl(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[], VoidType(),Block([Return()])),
    #                     FuncDecl(Id('foo'),[], VoidType(),Block([Return()]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_FuncDecl(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[], VoidType(),Block([Return()])),
    #                     FuncDecl(Id('foo'),[], IntType(),Block([]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test6(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[VarDecl("a", IntType())], VoidType(),Block([Return()]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test7(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[VarDecl("a", IntType()), VarDecl("a", IntType())], VoidType(),Block([Return()]))
    #                     ])
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,407))


    # def test8(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[VarDecl("a", IntType()), VarDecl("a", FloatType())], VoidType(),Block([Return()]))
    #                     ])
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,408))


    # def test9(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),[VarDecl("a", IntType()), VarDecl("b", IntType())], VoidType(),Block([Return()]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test10(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('a', ArrayPointerType(FloatType())), 
    #                                         VarDecl("b", IntType())], 
    #                                         VoidType(),
    #                                         Block([Return()]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,410))


    # def test11(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('a', ArrayPointerType(FloatType())), 
    #                                         VarDecl("b", IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl("b", IntType()),
    #                                             Return()
    #                                         ]))
    #                     ])
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,411))


    # def test12(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Return()
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,412))


    # def test13(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType()),
    #                                                 Return()
    #                                             ])
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,413))


    # def test14(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType()),
    #                                                 Return()
    #                                             ])
    #                                         ])),
    #                     FuncDecl(Id('foo'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType()),
    #                                                 Return()
    #                                             ])
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,414))


    # def test15(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType()),
    #                                                 Return()
    #                                             ])
    #                                         ])),
    #                     FuncDecl(Id('foo'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType())
    #                                             ]),
    #                                             Block([
    #                                                 VarDecl('a', IntType())
    #                                             ]),
    #                                             Return()
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,415))


    # def test16(self):

    #     input = Program([
    #                     VarDecl('a', ArrayPointerType(FloatType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType())
    #                                             ]),
    #                                             Return()
    #                                         ])),
    #                     FuncDecl(Id('foo'),[
    #                                         VarDecl('b', ArrayPointerType(FloatType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             Block([
    #                                                 VarDecl('a', IntType()),
    #                                                 Block([
    #                                                     VarDecl('a', IntType())
    #                                                 ])
    #                                             ]),
    #                                             Block([
    #                                                 VarDecl('a', IntType())
    #                                             ]),
    #                                             Return()
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,416))
    
    # def test17(self):

    #     input = Program([
    #                     VarDecl("a", IntType()),
    #                     FuncDecl(Id('main'),
    #                         [], 
    #                         VoidType(),
    #                         Block([
    #                             BinaryOp('+',Id('a'),Id('b'))
    #                         ]))
    #                     ])
    #     expect = "Undeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test18(self):

    #     input = Program([
    #                     VarDecl('a' ,ArrayType(10, BoolType())),
    #                     FuncDecl(Id('main'),[
    #                                         VarDecl('b' ,ArrayType(10, BoolType())), 
    #                                         VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', IntType()),
    #                                             BinaryOp('+',Id('a'),Id('b')),
    #                                             Block([
    #                                                 VarDecl('a', IntType()),
    #                                                 BinaryOp('+',Id('a'),Id('b'))
    #                                             ])
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,418))


    # def test19(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([])),
    #                     FuncDecl(Id('main'),[VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             CallExpr(Id('foo'),[IntLiteral(1)])
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,419))


    # def test20(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([])),
    #                     FuncDecl(Id('main'),[VarDecl('c', IntType())], 
    #                                         VoidType(),
    #                                         Block([
    #                                             CallExpr(Id('foo'),[])
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test21(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([])),
    #                     FuncDecl(Id('main'),[], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', FloatType()),
    #                                             VarDecl('b', IntType()),
    #                                             BinaryOp('-',Id('a'),Id('b'))
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,421))


    # def test22(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([Return(None)])),
    #                     FuncDecl(Id('main'),[], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', FloatType()),
    #                                             VarDecl('b', IntType()),
    #                                             VarDecl('main', IntType()),
    #                                             BinaryOp('/',Id('a'),Id('b')),
    #                                             CallExpr(Id('foo'),[Id('b')]),
    #                                             Return(None)
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,422))



    # def test23(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([Return(None)])),
    #                     FuncDecl(Id('main'),[], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', BoolType()),
    #                                             VarDecl('b', IntType()),
    #                                             VarDecl('main', IntType()),
    #                                             If(Id('a'),BinaryOp('=',Id('b'),IntLiteral(1)), None),
    #                                             Return(None)
    #                                         ]))
    #                     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,423))


    # def test24(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([Return(None)])),
    #                     FuncDecl(Id('main'),[], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', BoolType()),
    #                                             VarDecl('b', IntType()),
    #                                             VarDecl('main', IntType()),
    #                                             Break(),
    #                                             If(Id('a'),BinaryOp('=',Id('b'),IntLiteral(1)), None),
    #                                             Return(None)
    #                                         ]))
    #                     ])
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,424))


    # def test25(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([Return(None)])),
    #                     FuncDecl(Id('main'),[], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', BoolType()),
    #                                             VarDecl('b', IntType()),
    #                                             VarDecl('main', IntType()),
    #                                             Continue(),
    #                                             If(Id('a'),BinaryOp('=',Id('b'),IntLiteral(1)), None),
    #                                             Return(None)
    #                                         ]))
    #                     ])
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,425))


    # def test26(self):

    #     input = Program([
    #                     FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([Return(None)])),
    #                     FuncDecl(Id('main'),[], 
    #                                         VoidType(),
    #                                         Block([
    #                                             VarDecl('a', BoolType()),
    #                                             VarDecl('b', IntType()),
    #                                             VarDecl('main', IntType()),
    #                                             If(Id('a'),BinaryOp('=',Id('b'),IntLiteral(1)), None),
    #                                             Dowhile([Break()],Id('a')),
    #                                             Return(None)
    #                                         ]))
    #                     ])
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,426))


    def test27(self):

        input = Program([
                        FuncDecl(Id('foo'), [VarDecl('a', IntType())], IntType(), Block([Return(None)])),
                        FuncDecl(Id('main'),[], 
                                            VoidType(),
                                            Block([
                                                VarDecl('a', BoolType()),
                                                VarDecl('b', IntType()),
                                                VarDecl('main', IntType()),
                                                For(IntLiteral(1),Id('a'),IntLiteral(1),Block([Break()])),
                                                Return(None)
                                            ]))
                        ])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,427))