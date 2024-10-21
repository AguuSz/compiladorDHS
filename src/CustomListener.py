from compiladorListener import compiladorListener
from compiladorParser import compiladorParser
from ValuesTable import *


class CustomListener(compiladorListener):
    def __init__(self):
        self.valuesTable = ValuesTable()
        # Almacena los identificadores (variables o funciones) a medida que se van declarando.
        self.idList = {}
        # Guarda las variables que han sido inicializadas.
        self.initializedList = []
        # Almacena los parámetros de las funciones.
        self.parametersList = {}
        # Cuenta el contexto en el que se esta trabajando
        self.counter = 0

    def write_context(self, context_number):
        self.f.write(f"Contexto: {context_number}\n")
        if self.valuesTable.ts[-1]:
            for each in self.valuesTable.ts[-1]:
                entry = self.valuesTable.ts[-1][each]
                print("Entry kind: ", entry.getKind())
                self.f.write(
                    f"{self.valuesTable.ts[-1][each].getType()} {each} ({self.valuesTable.ts[-1][each].getKind()}), "
                )
            self.f.write("\n")
        else:
            self.f.write("Vacio\n")

    def enterPrograma(self, ctx: compiladorParser.ProgramaContext):
        self.f = open("./output/tablaSimbolosss.txt", "w")

    def exitPrograma(self, ctx: compiladorParser.ProgramaContext):
        # Si el contador de contextos es mayor a 0, significa que hay contextos que no se han cerrado
        if self.counter >= 0:
            self.write_context(self.counter)

        for variable in self.idList:
            if variable not in self.initializedList and self.idList[variable] == "variable" and variable in self.valuesTable.ts[-1]:
                print(
                    f'WARNING: La variable "{variable}" fue declarada pero no inicializada.'
                )

        # Cerramos el archivo de salida
        self.f.close()
        # Eliminamos el contexto actual de la tabla de símbolos
        self.valuesTable.del_context()

        # Imprimimos mensajes de éxito
        print("Tabla de simbolos generada con exito!")
        print("Se ha guardado en el archivo ./output/tablaSimbolosss.txt")

    def enterBloqueInstruccion(self, ctx: compiladorParser.BloqueInstruccionContext):
        # Agregamos el contexto a la tabla de símbolos
        self.valuesTable.add_context()
        # Incrementamos el contador de contextos
        self.counter += 1

        # Si hay parametros en la lista de parametros, los agregamos al contexto actual
        if self.parametersList:
            for parameter in self.parametersList.keys():
                # Corroboramos si el parametro ya existe en el contexto actual
                if not self.valuesTable.findKey(parameter):
                    # Si no existe, lo agregamos al contexto actual
                    self.valuesTable.ts[-1][parameter] = variable(
                        parameter, self.parametersList[parameter]
                    )
                else:
                    print(
                        f'ERROR: La variable "{parameter}" ya existe en este contexto'
                    )
        # Limpiamos la lista de parametros despues de haberla agregado al contexto
        self.parametersList.clear()

    def exitBloqueInstruccion(self, ctx: compiladorParser.BloqueInstruccionContext):
        self.write_context(self.counter)
        self.counter -= 1
        self.valuesTable.del_context()

    def enterDoWhileInstruccion(self, ctx: compiladorParser.DoWhileInstruccionContext):
        pass

    def exitDoWhileInstruccion(self, ctx: compiladorParser.DoWhileInstruccionContext):
        pass

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

    def enterAsignacion(self, ctx: compiladorParser.AsignacionContext):
        pass

    def exitAsignacion(self, ctx: compiladorParser.AsignacionContext):
        name = ctx.getChild(0).getText()
        if self.valuesTable.findKey(str(name)):
            self.initializedList.append(str(name))
        else:
            # Uso de un identificador no declarado
            print(f'ERROR: La variable "{name}" no está declarada')

    def enterAsignacionFuncion(self, ctx: compiladorParser.AsignacionFuncionContext):
        pass

    def exitAsignacionFuncion(self, ctx: compiladorParser.AsignacionFuncionContext):
        key = ctx.getChild(2).getText()
        if not self.valuesTable.findKey(key):
            print(
                f'ERROR: La función "{key}" no está declarada o no existe en este contexto'
            )

    def enterDeclaracionVariable(
        self, ctx: compiladorParser.DeclaracionVariableContext
    ):
        pass

    def exitDeclaracionVariable(self, ctx: compiladorParser.DeclaracionVariableContext):
        name = ctx.getChild(1).getText()
        if self.valuesTable.findKey(name):
            # Doble declaración del mismo identificador
            print(f'ERROR: El identificador "{name}" ya fue declarado.')
            if name in self.initializedList:
                self.initializedList.remove(name)  # Remover de la lista de inicializados para evitar warning
        else:
            self.idList[name] = "variable"
            self.valuesTable.ts[-1][name] = variable(name, "variable")
            if ctx.getChildCount() > 3 and ctx.getChild(2).getText() == "=":
                # Si la variable se inicializa en el momento de la declaración
                self.initializedList.append(name)

    def enterDeclaracionFuncion(self, ctx: compiladorParser.DeclaracionFuncionContext):
        pass

    def exitDeclaracionFuncion(self, ctx: compiladorParser.DeclaracionFuncionContext):
        name = ctx.getChild(1).getText()
        if self.valuesTable.findKey(name):
            # Doble declaración del mismo identificador
            print(f'ERROR: La función "{name}" ya fue declarada.')
        else:
            self.idList[name] = "function"
            self.valuesTable.ts[-1][name] = variable(name, "function")

    def enterParametro(self, ctx: compiladorParser.ParametroContext):
        pass

    def exitParametro(self, ctx: compiladorParser.ParametroContext):
        name = str(ctx.getChild(1).getText())
        tipo = str(ctx.getChild(0).getText())
        if not self.valuesTable.findKey(name):
            self.parametersList[name] = tipo