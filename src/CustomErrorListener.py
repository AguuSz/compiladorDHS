from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error sintáctico en la línea {line}:{column} - {msg}")
