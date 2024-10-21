grammar compilador;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
CA: '[';
CC: ']';
PYC: ';';
COMA: ',';

SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
MOD: '%';

ASIG: '=';
IGUAL: '==';
MAYOR: '>';
MENOR: '<';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
DISTINTO: '!=';

AND: '&&';
OR: '||';
NOT: '!';

INCREMENTO: '++';
DECREMENTO: '--';

NUMERO: DIGITO+;
FLOTANTES: DIGITO+ '.' DIGITO+;
FLOTANTESNEGATIVOS: '-' FLOTANTES;

INT: 'int';
DO: 'do';
WHILE: 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
RETURN: 'return';

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r]+ -> skip;
OTRO: .;

// Raíz del árbol
programa: instrucciones EOF | PYC;

instrucciones: instruccion+;

instruccion:
    doWhileInstruccion // PYC
    | whileInstruccion
    | ifInstruccion
    | forInstruccion
    | returnInstruccion // PYC
    | asignacion // PYC
    | asignacionFuncion // PYC
    | llamadoFuncionInstruccion // PYC
    | comparacionInstruccion
    | operacionInstruccion // PYC
    | declaracionFuncion
    | declaracionVariable // PYC
    | bloqueInstruccion;

// TODO: separar declaracion de variable y funcion en 2 separados y actualizar el listener.

declaracionVariable:
    tipo ID (COMA ID)* PYC
    | tipo ID (ASIG expresion)? (COMA ID (ASIG expresion)?)* PYC;

declaracionFuncion: tipo ID PA parametros PC bloqueInstruccion;

parametros:
    parametro (COMA parametro)*
    | /* vacío: permite funciones sin parámetros */;

parametro: tipo ID;

tipo: INT;

doWhileInstruccion:
    DO bloqueInstruccion WHILE PA instruccion PC PYC;

whileInstruccion: WHILE PA instruccion PC instruccion;

ifInstruccion:
    IF PA comparacionInstruccion PC bloqueInstruccion (
        ELSE instruccion
    )?;

forInstruccion:
    FOR PA declaracionVariable comparacionInstruccion PYC operacionInstruccionFor PC
        bloqueInstruccion;

bloqueInstruccion: LLA instrucciones LLC;

comparacionInstruccion:
    ID comparador ID
    | ID comparador NUMERO
    | NUMERO comparador NUMERO
    | NUMERO comparador ID;

comparador:
    IGUAL
    | MAYOR
    | MENOR
    | MAYORIGUAL
    | MENORIGUAL
    | DISTINTO;

operacionInstruccion:
    expresion PYC
    | incremento PYC
    | decremento PYC;

// Aca me hubiese gustado poner un ? para hacer que sea opcional, pero no consideraria los incrementos y decrementos que no son para los FOR
operacionInstruccionFor: expresion | incremento | decremento;

expresion: termino sumaResta | lor logicoOR;

logicoOR: logicoAND logicoY;
lor: OR logicoOR lor |;

logicoAND: termino sumaResta;

logicoY: AND logicoY logicoAND |;

termino: factor multiplicacionDivision;

sumaResta: SUMA termino sumaResta | RESTA termino sumaResta |;

factor: ID | NUMERO | PA expresion PC;

multiplicacionDivision:
    MULT factor multiplicacionDivision
    | DIV factor multiplicacionDivision
    |;

llamadoFuncionInstruccion: ID PA parametrosFuncion PC PYC;

parametrosFuncion: expresion (COMA expresion)*;

incremento: ID INCREMENTO;
decremento: ID DECREMENTO;

returnInstruccion: RETURN expresion? PYC;

asignacion: ID ASIG expresion PYC;
asignacionFuncion: ID ASIG ID PA parametrosFuncion PC PYC;