from compiladorListener import compiladorListener
from compiladorParser import compiladorParser
from ValuesTable import *
from antlr4 import TerminalNode


class CustomListener(compiladorListener):
    def __init__(self):
        self.valuesTable = ValuesTable()
        # Almacena los identificadores (variables o funciones) a medida que se van declarando.
        self.idList = {}
        # Guarda las variables que han sido inicializadas.
        self.initializedList = []
        # Almacena los parámetros de las funciones.
        self.parametersList = {}
        # Cuenta el contexto en el que se está trabajando
        self.counter = 0

        self.show_warnings = False
        self.file = "./output/tablaSimbolos.txt"

    def write_context(self, context_number):
        self.f.write(f"Contexto: {context_number}\n")
        if self.valuesTable.ts[-1]:
            for each in self.valuesTable.ts[-1]:
                entry = self.valuesTable.ts[-1][each]
                self.f.write(
                    f"{self.valuesTable.ts[-1][each].getType()} {each} ({self.valuesTable.ts[-1][each].getKind()}), "
                )
            self.f.write("\n")
        else:
            self.f.write("Vacio\n")

    def enterPrograma(self, ctx: compiladorParser.ProgramaContext):
        self.f = open(self.file, "w")
        print("Warnings activadas: " + str(self.show_warnings) + "\n")

    def exitPrograma(self, ctx: compiladorParser.ProgramaContext):
        # Si el contador de contextos es mayor a 0, significa que hay contextos que no se han cerrado
        if self.counter >= 0:
            self.write_context(self.counter)

        for variable in self.idList:
            if (
                variable not in self.initializedList
                and self.idList[variable]["kind"] == "variable"
                and variable in self.valuesTable.ts[-1]
            ):
                if self.show_warnings:
                    line = self.idList[variable]["line"]
                    print(
                        f'[{line}] WARNING: La variable "{variable}" fue declarada pero no inicializada.'
                    )

        # Cerramos el archivo de salida
        self.f.close()
        # Eliminamos el contexto actual de la tabla de símbolos
        self.valuesTable.del_context()

        # Imprimimos mensajes de éxito
        print("\nTabla de símbolos generada con éxito!")
        print("Se ha guardado en el archivo " + self.file)

    def enterBloqueInstruccion(self, ctx: compiladorParser.BloqueInstruccionContext):
        # Agregamos el contexto a la tabla de símbolos
        self.valuesTable.add_context()
        # Incrementamos el contador de contextos
        self.counter += 1

        # Si hay parámetros en la lista de parámetros, los agregamos al contexto actual
        if self.parametersList:
            for parameter in self.parametersList.keys():
                # Corroboramos si el parámetro ya existe en el contexto actual
                if not self.valuesTable.findKey(parameter):
                    # Si no existe, lo agregamos al contexto actual
                    self.valuesTable.ts[-1][parameter] = variable(
                        parameter, self.parametersList[parameter]
                    )
                else:
                    line = ctx.start.line
                    print(
                        f'[{line}] ERROR: La variable "{parameter}" ya existe en este contexto'
                    )
        # Limpiamos la lista de parámetros después de haberla agregado al contexto
        self.parametersList.clear()

    def exitBloqueInstruccion(self, ctx: compiladorParser.BloqueInstruccionContext):
        self.write_context(self.counter)
        self.counter -= 1
        self.valuesTable.del_context()

    def enterDoWhileInstruccion(self, ctx: compiladorParser.DoWhileInstruccionContext):
        pass

    def exitDoWhileInstruccion(self, ctx: compiladorParser.DoWhileInstruccionContext):
        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if last_child.getText() != ";":
            line = ctx.start.line
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')

    def enterForInstruccion(self, ctx: compiladorParser.ForInstruccionContext):
        self.valuesTable.add_context()
        self.counter += 1

    def exitForInstruccion(self, ctx: compiladorParser.ForInstruccionContext):
        self.write_context(self.counter)
        self.counter -= 1
        self.valuesTable.del_context()

    def enterWhileInstruccion(self, ctx: compiladorParser.WhileInstruccionContext):
        self.valuesTable.add_context()
        self.counter += 1

    def exitWhileInstruccion(self, ctx: compiladorParser.WhileInstruccionContext):
        self.write_context(self.counter)
        self.counter -= 1
        self.valuesTable.del_context()

    def enterIfInstruccion(self, ctx: compiladorParser.IfInstruccionContext):
        self.valuesTable.add_context()
        self.counter += 1

    def exitIfInstruccion(self, ctx: compiladorParser.IfInstruccionContext):
        self.write_context(self.counter)
        self.counter -= 1
        self.valuesTable.del_context()

    # Enter a parse tree produced by compiladorParser#comparacionInstruccion.
    def enterComparacionInstruccion(
        self, ctx: compiladorParser.ComparacionInstruccionContext
    ):
        pass

    # Exit a parse tree produced by compiladorParser#comparacionInstruccion.
    def exitComparacionInstruccion(
        self, ctx: compiladorParser.ComparacionInstruccionContext
    ):
        line = ctx.start.line
        first_child = ctx.getChild(0)
        if first_child.getSymbol().type == compiladorParser.ID:
            # Nos aseguramos que sea un ID
            # Comparamos si el ID está declarado o no y usado en la tabla de símbolos
            if not self.valuesTable.findKey(first_child.getText()):
                print(
                    f'[{line}] ERROR: La variable "{first_child.getText()}" no está declarada'
                )
            # Compruebo que la variable haya sido inicializada
            if self.show_warnings and first_child.getText() not in self.initializedList:
                print(
                    f'[{line}] WARNING: La variable "{first_child.getText()}" no ha sido inicializada'
                )

        third_child = ctx.getChild(2)
        if third_child.getSymbol().type == compiladorParser.ID:
            # Nos aseguramos que sea un ID
            # Comparamos si el ID está declarado o no y usado en la tabla de símbolos
            if not self.valuesTable.findKey(third_child.getText()):
                print(
                    f'[{line}] ERROR: La variable "{third_child.getText()}" no está declarada'
                )
            if self.show_warnings and third_child.getText() not in self.initializedList:
                print(
                    f'[{line}] WARNING: La variable "{third_child.getText()}" no ha sido inicializada'
                )

    # Enter a parse tree produced by compiladorParser#expresion.
    def enterFactor(self, ctx: compiladorParser.ExpresionContext):
        pass

    # Exit a parse tree produced by compiladorParser#expresion.
    def exitFactor(self, ctx: compiladorParser.ExpresionContext):
        line = ctx.start.line
        first_child = ctx.getChild(0)
        if first_child.getSymbol().type == compiladorParser.ID:
            # Nos aseguramos que sea un ID
            # Comparamos si el ID está declarado o no y usado en la tabla de símbolos
            if not self.valuesTable.findKey(first_child.getText()):
                print(
                    f'[{line}] ERROR: La variable "{first_child.getText()}" no está declarada'
                )

            # Compruebo que la variable haya sido inicializada
            if self.show_warnings and first_child.getText() not in self.initializedList:
                print(
                    f'[{line}] WARNING: La variable "{first_child.getText()}" no ha sido inicializada'
                )

    def enterAsignacion(self, ctx: compiladorParser.AsignacionContext):
        pass

    def exitAsignacion(self, ctx: compiladorParser.AsignacionContext):
        line = ctx.start.line
        name = ctx.getChild(0).getText()
        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if self.valuesTable.findKey(str(name)):
            self.initializedList.append(str(name))
        else:
            # Uso de un identificador no declarado
            print(f'[{line}] ERROR: La variable "{name}" no está declarada')

        if last_child.getText() != ";":
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')

    def enterAsignacionFuncion(self, ctx: compiladorParser.AsignacionFuncionContext):
        pass

    def exitAsignacionFuncion(self, ctx: compiladorParser.AsignacionFuncionContext):
        line = ctx.start.line
        key = ctx.getChild(2).getText()
        if not self.valuesTable.findKey(key):
            print(
                f'[{line}] ERROR: La función "{key}" no está declarada o no existe en este contexto'
            )

        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if last_child.getText() != ";":
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')

    def enterDeclaracionVariable(
        self, ctx: compiladorParser.DeclaracionVariableContext
    ):
        pass

    def exitDeclaracionVariable(self, ctx: compiladorParser.DeclaracionVariableContext):
        line = ctx.start.line
        for i in range(0, ctx.getChildCount()):
            if isinstance(ctx.getChild(i), TerminalNode):
                if ctx.getChild(i).getSymbol().type == compiladorParser.ID:
                    name = ctx.getChild(i).getText()
                    if self.valuesTable.findKey(name):
                        # Doble declaración del mismo identificador
                        print(
                            f'[{line}] ERROR: El identificador "{name}" ya fue declarado.'
                        )
                        if name in self.initializedList:
                            self.initializedList.remove(name)
                    else:
                        self.idList[name] = {"kind": "variable", "line": line}
                        self.valuesTable.ts[-1][name] = variable(name, "variable")
                        if ctx.getChild(i + 1).getText() == "=":
                            # Si la variable se inicializa en el momento de la declaración
                            self.initializedList.append(name)
        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if last_child.getText() != ";":
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')

    def enterDeclaracionFuncion(self, ctx: compiladorParser.DeclaracionFuncionContext):
        pass

    def exitDeclaracionFuncion(self, ctx: compiladorParser.DeclaracionFuncionContext):
        line = ctx.start.line
        name = ctx.getChild(1).getText()
        if self.valuesTable.findKey(name):
            # Doble declaración del mismo identificador
            print(f'[{line}] ERROR: La función "{name}" ya fue declarada.')
        else:
            self.idList[name] = {"kind": "function", "line": line}
            self.valuesTable.ts[-1][name] = variable(name, "function")

    def enterParametro(self, ctx: compiladorParser.ParametroContext):
        pass

    def exitParametro(self, ctx: compiladorParser.ParametroContext):
        type = str(ctx.getChild(0).getText())
        name = str(ctx.getChild(1).getText())
        if not self.valuesTable.findKey(name):
            self.parametersList[name] = type

    # Enter a parse tree produced by compiladorParser#returnInstruccion.
    def enterReturnInstruccion(self, ctx: compiladorParser.ReturnInstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#returnInstruccion.
    def exitReturnInstruccion(self, ctx: compiladorParser.ReturnInstruccionContext):
        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if last_child.getText() != ";":
            line = ctx.start.line
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')

    # Enter a parse tree produced by compiladorParser#llamadoFuncionInstruccion.
    def enterLlamadoFuncionInstruccion(
        self, ctx: compiladorParser.LlamadoFuncionInstruccionContext
    ):
        pass

    # Exit a parse tree produced by compiladorParser#llamadoFuncionInstruccion.
    def exitLlamadoFuncionInstruccion(
        self, ctx: compiladorParser.LlamadoFuncionInstruccionContext
    ):
        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if last_child.getText() != ";":
            line = ctx.start.line
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')

    # Enter a parse tree produced by compiladorParser#operacionInstruccion.
    def enterOperacionInstruccion(
        self, ctx: compiladorParser.OperacionInstruccionContext
    ):
        pass

    # Exit a parse tree produced by compiladorParser#operacionInstruccion.
    def exitOperacionInstruccion(
        self, ctx: compiladorParser.OperacionInstruccionContext
    ):
        last_child = ctx.getChild(ctx.getChildCount() - 1)
        if last_child.getText() != ";":
            line = ctx.start.line
            print(f'[{line}] ERROR: Falta un ";" al final de la instrucción')
