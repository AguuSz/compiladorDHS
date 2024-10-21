grammar compilador;

// Fragmentos para letras y dígitos
fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

// Símbolos y operadores
PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
CA : '[' ;
CC : ']' ;
PYC : ';' ;
COMA : ',' ;

SUMA : '+' ;
RESTA: '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;

ASIG: '=' ;
IGUAL: '==' ;
MAYOR: '>' ;
MENOR: '<' ;
MAYORIGUAL: '>=' ;
MENORIGUAL: '<=' ;
DISTINTO: '!=' ;

AND : '&&' ;
OR : '||' ;
NOT : '!' ;

INCREMENTO : '++' ;
DECREMENTO: '--' ;

// Tipos de datos y palabras reservadas
INT : 'int' ;
FLOAT : 'float' ;
VOID : 'void' ;
DO: 'do' ;
WHILE : 'while' ;
FOR : 'for' ;
IF : 'if' ;
ELSE: 'else' ;
RETURN: 'return' ;

// Literales e identificadores
NUMERO : DIGITO+ ;
FLOTANTE: DIGITO+ '.' DIGITO+ ;

ID: (LETRA | '_') (LETRA | DIGITO | '_')* ;

// Espacios en blanco
WS: [ \t\n\r]+ -> skip ;

// Tokens no reconocidos
OTRO : . ;

// Reglas de inicio
programa : instrucciones EOF ;

// Lista de instrucciones
instrucciones: instruccion* ;

// Definición de instrucciones
instruccion
    : declaracionVariable
    | declaracionFuncion
    | asignacion
    | asignacionFuncion
    | llamadoFuncionInstruccion
    | returnInstruccion
    | ifInstruccion
    | whileInstruccion
    | doWhileInstruccion
    | forInstruccion
    | bloqueInstruccion
    | expresion PYC
    ;

declaracionVariable
    : tipo listaDeclaracionVariable PYC
    ;

listaDeclaracionVariable
    : declaradorVariable (COMA declaradorVariable)*
    ;

declaradorVariable
    : ID
    | ID ASIG inicializador
    ;

inicializador
    : expresion
    ;

declaracionFuncion
    : tipo ID PA listaParametros? PC bloqueInstruccion
    ;

listaParametros
    : parametro (COMA parametro)*
    ;

parametro
    : tipo ID
    ;

tipo
    : INT
    | FLOAT
    | VOID
    ;

asignacion
    : ID ASIG expresion PYC
    ;

asignacionFuncion
    : ID ASIG llamadoFuncion
    ;

llamadoFuncionInstruccion
    : llamadoFuncion PYC
    ;

llamadoFuncion
    : ID PA argumentos? PC
    ;

argumentos
    : expresion (COMA expresion)*
    ;

returnInstruccion
    : RETURN expresion? PYC
    ;

ifInstruccion
    : IF PA expresion PC instruccion (ELSE instruccion)?
    ;

whileInstruccion
    : WHILE PA expresion PC instruccion
    ;

doWhileInstruccion
    : DO instruccion WHILE PA expresion PC PYC
    ;

forInstruccion
    : FOR PA inicializacionFor condicionFor PYC actualizacionFor PC instruccion
    ;

inicializacionFor
    : declaracionVariable
    | asignacion
    | 
    ;

condicionFor
    : expresion
    | 
    ;

actualizacionFor
    : expresion
    | 
    ;

bloqueInstruccion
    : LLA instrucciones LLC
    ;

expresion
    : expresionLogica
    ;

expresionLogica
    : expresionLogica OR expresionLogicaSecundaria
    | expresionLogicaSecundaria
    ;

expresionLogicaSecundaria
    : expresionLogicaSecundaria AND expresionIgualdad
    | expresionIgualdad
    ;

expresionIgualdad
    : expresionIgualdad operadorIgualdad expresionRelacional
    | expresionRelacional
    ;

operadorIgualdad
    : IGUAL
    | DISTINTO
    ;

expresionRelacional
    : expresionRelacional operadorRelacional expresionAditiva
    | expresionAditiva
    ;

operadorRelacional
    : MAYOR
    | MENOR
    | MAYORIGUAL
    | MENORIGUAL
    ;

expresionAditiva
    : expresionAditiva operadorAditivo expresionMultiplicativa
    | expresionMultiplicativa
    ;

operadorAditivo
    : SUMA
    | RESTA
    ;

expresionMultiplicativa
    : expresionMultiplicativa operadorMultiplicativo expresionUnaria
    | expresionUnaria
    ;

operadorMultiplicativo
    : MULT
    | DIV
    | MOD
    ;

expresionUnaria
    : operadorUnario expresionUnaria
    | expresionPrimaria
    ;

operadorUnario
    : SUMA
    | RESTA
    | NOT
    ;

expresionPrimaria
    : PA expresion PC
    | literal
    | ID
    | llamadoFuncion
    ;

literal
    : NUMERO
    | FLOTANTE
    ;
