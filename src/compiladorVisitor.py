# Generated from compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#programa.
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracionVariable.
    def visitDeclaracionVariable(self, ctx:compiladorParser.DeclaracionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracionFuncion.
    def visitDeclaracionFuncion(self, ctx:compiladorParser.DeclaracionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros.
    def visitParametros(self, ctx:compiladorParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametro.
    def visitParametro(self, ctx:compiladorParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#doWhileInstruccion.
    def visitDoWhileInstruccion(self, ctx:compiladorParser.DoWhileInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#whileInstruccion.
    def visitWhileInstruccion(self, ctx:compiladorParser.WhileInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ifInstruccion.
    def visitIfInstruccion(self, ctx:compiladorParser.IfInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#forInstruccion.
    def visitForInstruccion(self, ctx:compiladorParser.ForInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloqueInstruccion.
    def visitBloqueInstruccion(self, ctx:compiladorParser.BloqueInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#comparacionInstruccion.
    def visitComparacionInstruccion(self, ctx:compiladorParser.ComparacionInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#comparador.
    def visitComparador(self, ctx:compiladorParser.ComparadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#operacionInstruccion.
    def visitOperacionInstruccion(self, ctx:compiladorParser.OperacionInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#operacionInstruccionFor.
    def visitOperacionInstruccionFor(self, ctx:compiladorParser.OperacionInstruccionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expresion.
    def visitExpresion(self, ctx:compiladorParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#logicoOR.
    def visitLogicoOR(self, ctx:compiladorParser.LogicoORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lor.
    def visitLor(self, ctx:compiladorParser.LorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#logicoAND.
    def visitLogicoAND(self, ctx:compiladorParser.LogicoANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#logicoY.
    def visitLogicoY(self, ctx:compiladorParser.LogicoYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#termino.
    def visitTermino(self, ctx:compiladorParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#sumaResta.
    def visitSumaResta(self, ctx:compiladorParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#multiplicacionDivision.
    def visitMultiplicacionDivision(self, ctx:compiladorParser.MultiplicacionDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#llamadoFuncionInstruccion.
    def visitLlamadoFuncionInstruccion(self, ctx:compiladorParser.LlamadoFuncionInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametrosFuncion.
    def visitParametrosFuncion(self, ctx:compiladorParser.ParametrosFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#incremento.
    def visitIncremento(self, ctx:compiladorParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#decremento.
    def visitDecremento(self, ctx:compiladorParser.DecrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#returnInstruccion.
    def visitReturnInstruccion(self, ctx:compiladorParser.ReturnInstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacionFuncion.
    def visitAsignacionFuncion(self, ctx:compiladorParser.AsignacionFuncionContext):
        return self.visitChildren(ctx)



del compiladorParser