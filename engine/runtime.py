
class XLSLRuntime:
    def execute(self, ast):
        return {"executed": True, "ast_nodes": len(ast)}
