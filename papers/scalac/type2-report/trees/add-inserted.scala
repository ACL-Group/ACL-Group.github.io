class Add {
	def add(x: Int): Int = {
		ScalaTrace.logger.log("add$ >>> x")
		ScalaTrace.logger.log("x 1 >>> add")
		x + 1
	}
	
	def callAdd() {
		ScalaTrace.logger.log("8 >>> add$")
		val addResult = add(8)
		ScalaTrace.logger.log("add >>> addResult")
	}
}

def genLog(dataDependence: String, positionInSourceFile: Position): Tree = {
    def extractEssentialPath(path: String): String = {         
    	if(path.contains("NoPosition"))
            "NoPosition"
        else
            path.substring(path.indexOf("/src/") + 4)
        }
      
    val liter0 = Literal(Constant(extractEssentialPath(positionInSourceFile.focus.toString)))
    liter0.setType(typeOf[String])
    
    val liter1 = Literal(Constant(dataDependence)) 
    liter1.setType(typeOf[String])   
                  
    val scalatrace = rootMirror.staticModule("ScalaTrace")
    val logger = definitions.getMember(scalatrace, newTermName("logger"))
    val callLog = global.gen.mkMethodCall(logger, newTermName("log"), List(liter0, liter1))
    val Apply(fun, _) = callLog
    fun.setSymbol(logger.info.decl(newTermName("log")))
    fun.setType(logger.info.decl(newTermName("log")).tpe)  
    val Select(qual, _) = fun
    qual.setType(logger.tpe)
    callLog.setType(typeOf[Unit])
    callLog
}


