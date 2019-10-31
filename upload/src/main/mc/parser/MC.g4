// grammar MC;

// @lexer::header {
// from lexererr import *
// }

// @lexer::member {
// def emit(self):
//     tk = self.type
//     if tk == UNCLOSE_STRING:       
//         result = super.emit();
//         raise UncloseString(result.text);
//     elif tk == ILLEGAL_ESCAPE:
//         result = super.emit();
//         raise IllegalEscape(result.text);
//     elif tk == ERROR_CHAR:
//         result = super.emit();
//         raise ErrorToken(result.text); 
//     else:
//         return super.emit();
// }

// options{
// 	language=Python3;
// }

// program  : mctype 'main' LB RB LP body? RP EOF ;

// mctype: INTTYPE | VOIDTYPE ;

// body: funcall SEMI;

// exp: funcall | INTLIT ;

// funcall: ID LB exp? RB ;

// INTTYPE: 'int' ;

// VOIDTYPE: 'void'  ;

// ID: [a-zA-Z]+ ;

// INTLIT: [0-9]+;

// LB: '(' ;

// RB: ')' ;

// LP: '{';

// RP: '}';

// SEMI: ';' ;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;

// 1711502
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    elif tk == self.STRINGLIT:
        result = super().emit();
        result.text = result.text[1:-1]
        return result 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : decl+ EOF ;

decl
            : var_decl 
            | func_decl
            ;

var_decl
            : primary_type var (COMMA var)* SEMI;

primary_type
            : BOOLEANTYPE 
            | INTTYPE 
            | FLOATTYPE 
            | STRINGTYPE
            ;

var 
            : ID 
            | element
            ;       

element
            : ID LSB INTLIT RSB
            ;    

func_decl
            : mctype ID LB list_params RB block_stmt
            ;

mctype
            : primary_type
            | VOIDTYPE
            | output_ptr_type
            ;

output_ptr_type
            : primary_type LSB RSB
            ;

list_params
            : (param_decl (COMMA param_decl)*)?
            ;

param_decl  
            : primary_type ID
            | primary_type ID LSB RSB
            ;

call_func
            : ID LB list_exprs RB
            ;

list_exprs
            : (expr (COMMA expr)*)?
            ;


if_stmt
            : IF LB expr RB stmt (ELSE stmt)?
            ;

do_while_stmt
            : DO (stmt)+ WHILE expr SEMI
            ; 

for_stmt
            : FOR LB expr SEMI expr SEMI expr RB stmt
            ;

break_stmt
            : BREAK SEMI
            ;

continue_stmt
            : CONTINUE SEMI
            ;

return_stmt
            : RETURN expr? SEMI
            ;

expr_stmt
            : expr SEMI
            ;   

stmt
            : if_stmt 
            | do_while_stmt
            | for_stmt
            | break_stmt
            | continue_stmt
            | return_stmt
            | expr_stmt
            | block_stmt       
            ;

block_stmt
            : LP stmt_var_decl* RP
            ;
            
stmt_var_decl 
            : stmt
            | var_decl
            ;

expr
            : expr1 ASSIGN_OP expr
            | expr1
            ;

expr1           : expr1 OR_OP expr2
            | expr2
            ;

expr2
            : expr2 AND_OP expr3
            | expr3
            ;

expr3
            : expr4 (EQUAL_OP | NOT_EQUAL_OP) expr4
            | expr4
            ;

expr4
            : expr5 (LESS_OP | LESS_EQUAL_OP | GREATER_EQUAL_OP | GREATER_OP) expr5
            | expr5
            ;

expr5
            : expr5 (ADD_OP | SUB_OP) expr6
            | expr6
            ;

expr6 
            : expr6 (DIV_OP | MUL_OP | MODULUS_OP) expr7
            | expr7
            ;

expr7
            : (SUB_OP |NOT_OP) expr7
            | expr8
            ;

expr8
            : expr9 LSB expr RSB
            | expr9
            ;


expr9
            : LB expr RB
            | call_func
            | lit
            | ID
            ;

 
lit         
            : INTLIT 
            | FLOATLIT 
            | BOOLLIT 
            | STRINGLIT
            ;
LB: '(' ;

RB: ')' ;

LSB: '[';

RSB: ']';

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',';

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines



// Comment

LINE_COMMENT: '//'~[\n\r]* -> skip;
BLOCK_COMMENT: '/*'(.)*?'*/'-> skip;
        

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLEANTYPE: 'boolean';

FLOATTYPE: 'float';

STRINGTYPE: 'string';

RETURN: 'return';

BREAK: 'break';

CONTINUE: 'continue';

IF: 'if';

ELSE: 'else';

FOR: 'for';

WHILE: 'while';

DO: 'do';

fragment TRUE: 'true';

fragment FALSE: 'false';

// Operator

ADD_OP: '+';

MUL_OP: '*';

NOT_OP: '!';

OR_OP: '||';

NOT_EQUAL_OP: '!=';

LESS_OP: '<';

LESS_EQUAL_OP: '<=';

ASSIGN_OP: '=';

SUB_OP: '-';

MODULUS_OP: '%';

DIV_OP: '/';

AND_OP: '&&';

EQUAL_OP: '==';

GREATER_OP: '>';

GREATER_EQUAL_OP: '>=';

// Literals


INTLIT: [0-9]+;


fragment Point: '.';
fragment Exponent: [Ee]('-'?)[0-9]+;
FLOATLIT
            : INTLIT Point INTLIT? Exponent?
            | Point INTLIT Exponent?
            | INTLIT Exponent
            ;


BOOLLIT
            : TRUE 
            | FALSE
            ;



ID: [a-zA-Z_][a-zA-Z0-9_]* ;
STRINGLIT: '"'('\\' [bfrnt"\\] | ~[\b\f\r\n\t\\"])*'"';

ILLEGAL_ESCAPE: '"' (~[\b\f\r\n\t\\"] | '\\' [bfrnt"\\])* ('\\'~[bfnrt"\\]);
UNCLOSE_STRING: '"' ( '\\' [bfrnt"\\] | ~[\b\f\r\n\t\\"] )*;

ERROR_CHAR: [?~`@#$^:.\\'&|];

