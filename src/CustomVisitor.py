from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser


class CustomVisitor(compiladorVisitor):
    def visitPrograma(self, ctx: compiladorParser.ProgramaContext):
        print("\n")
        print("-- Comienza a caminar")
        return super().visitPrograma(ctx)

    def visitBloqueInstruccion(self, ctx: compiladorParser.BloqueInstruccionContext):
        print("=" * 20 + "Nuevo contexto" + "=" * 20)
        print(ctx.getText())
        return super().visitBloqueInstruccion(ctx)

    def visitTerminal(self, node):
        # print(f"===>> Token: {node.getText()}")
        return super().visitTerminal(node)
