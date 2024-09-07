package <empty> {
  object hello extends scala.AnyRef {
    def <init>(): hello.type = {
      hello.super.<init>();
      ()
    };
    def main(args: Array[String]): Unit = {
      scala.this.Predef.println("Hello!");
      val adder: Add = new Add();
      adder.callAdd()
    }
  };
  class Add extends scala.AnyRef {
    def <init>(): Add = {
      Add.super.<init>();
      ()
    };
    def add(x: Int): Int = x.+(1);
    def callAdd(): Unit = {
      val addResult: Int = Add.this.add(8);
      ()
    }
  }
}

package <empty> {
  object hello extends scala.AnyRef {
    def <init>(): hello.type = {
      ScalaTrace.this.logger.log("hello.<init>$ >>> ", "/print/hello.scala,line-9,offset=140");
      {
        ScalaTrace.this.logger.log(" >>> java.lang.Object.<init>$", "/print/hello.scala,line-9,offset=140");
        hello.super.<init>()
      };
      {
        ScalaTrace.this.logger.log(" >>> Block193", "/print/hello.scala,line-1,offset=12");
        ScalaTrace.this.logger.log("Block193 >>> hello.<init>", "/print/hello.scala,line-9,offset=140");
        ()
      }
    };
    def main(args: Array[String]): Unit = {
      ScalaTrace.this.logger.log("hello.main$ >>>  hello.args", "/print/hello.scala,line-2,offset=22");
      scala.this.Predef.println({
        ScalaTrace.this.logger.log("  >>> scala.Predef.println$", "/print/hello.scala,line-3,offset=65");
        "Hello!"
      });
      val adder: Add = {
        ScalaTrace.this.logger.log(" >>> Add.<init>$", "/print/hello.scala,line-4,offset=96");
        ScalaTrace.this.logger.log("Add.<init> >>> hello.adder", "/print/hello.scala,line-4,offset=88");
        new Add()
      };
      {
        ScalaTrace.this.logger.log(" >>> Add.callAdd$", "/print/hello.scala,line-5,offset=127");
        ScalaTrace.this.logger.log("Add.callAdd >>> Block510", "/print/hello.scala,line-5,offset=127");
        ScalaTrace.this.logger.log("Block510 >>> hello.main", "/print/hello.scala,line-2,offset=48");
        adder.callAdd()
      }
    }
  };
  class Add extends scala.AnyRef {
    ...
    def add(x: Int): Int = {
       val newvalue = x.+({
        ScalaTrace.this.logger.log("Add.add$ >>>  Add.x", "/print/hello.scala,line-10,offset=160");
        1
      });
       ScalaTrace.this.logger.log("Add.x 1 >>> Add.add", "/print/hello.scala,line-11,offset=191");
    }
    def callAdd(): Unit = {
      ...
      val addResult: Int = Add.this.add({
        ScalaTrace.this.logger.log("8 >>> Add.add$", "/print/hello.scala,line-15,offset=253");
        8
      });
      ScalaTrace.this.logger.log("Add.add >>> Add.addResult", "/print/hello.scala,line-15,offset=238");
      ...     
    }
  }
}

class Add extends scala.AnyRef {
    ...
    def add(x: Int): Int = x.+(1);
    def callAdd(): Unit = {
      val addResult: Int = Add.this.add(8);
      ()
    }
  }

def genStraight(ctx: Context, msg: String, pos: Position) {

      def extractEssentialPath(path: String): String = {
          if(path.contains("NoPosition"))
            "NoPosition"
          else
            path.substring(path.indexOf("/src/") + 4, path.lastIndexOf(","))
      }

      val Apply(fun, args) = genPrint(msg, NoPosition)
      val Select(tree, _) = fun
      val Select(qualifier, selector) = tree
      val sym1 = tree.symbol
      val hostClass = findHostClass(qualifier.tpe, sym1)
      val qualSafeToElide = treeInfo isQualifierSafeToElide qualifier
      val isStatic = sym1.isStaticMember
      ctx.bb.emit(LOAD_FIELD(sym1, isStatic) setHostClass hostClass, tree.pos)
      ctx.bb.emit(CONSTANT(Constant(msg)), NoPosition)
      ctx.bb.emit(CONSTANT(Constant(extractEssentialPath(pos.focus.toString))), NoPosition)
      val sym = fun.symbol
      val cm = CALL_METHOD(sym, Dynamic)
      fun match {
        case Select(qual, _) =>
          val qualSym = findHostClass(qual.tpe, sym)
          if (qualSym == ArrayClass) {
            val kind = toTypeKind(qual.tpe)
            cm setTargetTypeKind kind
            log(s"Stored target type kind for {$sym.fullName} as $kind")
          }
          else {
            cm setHostClass qualSym
            if (qual.tpe.typeSymbol != qualSym)
              log(s"Precisified host class for $sym from ${qual.tpe.typeSymbol.fullName} to ${qualSym.fullName}")
          }
        case _ =>
      }
      ctx.bb.emit(cm, NoPosition)
      ctx.method.updateRecursive(sym)
      if (sym.isClassConstructor) UNIT
      else toTypeKind(sym.info.resultType)
}

class Add extends Object {
  // fields:

  // methods
  def add(x: Int (INT)): Int {
  locals: value x
  startBlock: 1
  blocks: [1]

  1:
    3   LOAD_LOCAL(value x)
    3   CONSTANT(1)
    3   CALL_PRIMITIVE(Arithmetic(ADD,INT))
    3   RETURN(INT)

  }
  Exception handlers:

  def callAdd(): Unit {
  locals: value addResult
  startBlock: 1
  blocks: [1]

  1:
    7   THIS(Add)
    7   CONSTANT(8)
    7   CALL_METHOD Add.add (dynamic)
    7   STORE_LOCAL(value addResult)
    7   SCOPE_ENTER value addResult
    7   SCOPE_EXIT value addResult
    7   RETURN(UNIT)

  }
  Exception handlers:

  def <init>(): Add {
  locals:
  startBlock: 1
  blocks: [1]

  1:
    11  THIS(Add)
    11  CALL_METHOD java.lang.Object.<init> (super())
    11  RETURN(UNIT)

  }
  Exception handlers:


}

class Add extends Object {
  // fields:

  // methods
  def add(x: Int (INT)): Int {
  locals: value x
  startBlock: 1
  blocks: [1]

  1:
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 Add.x @")
    ?   CONSTANT("Hello.scala,line-2")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##00 Add.add class: class Add")
    ?   CONSTANT("Hello.scala,line-2")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 Add.x")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    3   LOAD_LOCAL(value x)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 *")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    3   CONSTANT(1)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @operand1")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @operand2")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#3 @operand1 @operand2 @result")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 @result")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##04")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    3   CALL_PRIMITIVE(Arithmetic(ADD,INT))
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##05")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##01")
    ?   CONSTANT("NoPosition")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   RETURN(INT)

  }
  Exception handlers:

  def callAdd(): Unit {
  locals: value addResult
  startBlock: 1
  blocks: [1]

  1:
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##00 Add.callAdd class: class Add")
    ?   CONSTANT("Hello.scala,line-6")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 @this")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   THIS(Add)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 *")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   CONSTANT(8)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @this @")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   CALL_METHOD Add.add (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 Add.addResult")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   STORE_LOCAL(value addResult)
    7   SCOPE_ENTER value addResult
    7   SCOPE_EXIT value addResult
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##01")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   RETURN(UNIT)

  }
  Exception handlers:

  def <init>(): Add {
  locals:
  startBlock: 1
  blocks: [1]

  1:
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##02")
    ?   CONSTANT("Hello.scala,line-1")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##00 Add.<init> class: class Add")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 @this")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    11  THIS(Add)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @javaParam1")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##06")
    ?   CONSTANT("NoPosition")
    ?   CALL_METHOD Logger.log (dynamic)
    11  CALL_METHOD java.lang.Object.<init> (super())
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##07")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##01")
    ?   CONSTANT("NoPosition")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   RETURN(UNIT)

  }
  Exception handlers:




class Add extends Object {
  // fields:

  // methods
  def add(x: Int (INT)): Int {
  locals: value x
  startBlock: 1
  blocks: [1]

  1:
    3   LOAD_LOCAL(value x)
    3   CONSTANT(1)
    3   CALL_PRIMITIVE(Arithmetic(ADD,INT))
    3   RETURN(INT)

  }
  Exception handlers:

  def callAdd(): Unit {
  locals: value addResult
  startBlock: 1
  blocks: [1]

  1:
    7   THIS(Add)
    7   CONSTANT(8)
    7   CALL_METHOD Add.add (dynamic)
    7   STORE_LOCAL(value addResult)
    7   SCOPE_ENTER value addResult
    7   SCOPE_EXIT value addResult
    7   RETURN(UNIT)

  }
  Exception handlers:

  def <init>(): Add {
  locals:
  startBlock: 1
  blocks: [1]

  1:
    11  THIS(Add)
    11  CALL_METHOD java.lang.Object.<init> (super())
    11  RETURN(UNIT)

  }
  Exception handlers:


}

class Add extends Object {
  // fields:

  // methods
  def add(x: Int (INT)): Int {
  locals: value x
  startBlock: 1
  blocks: [1]

  1:
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 Add.x @")
    ?   CONSTANT("Hello.scala,line-2")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##00 Add.add class: class Add")
    ?   CONSTANT("Hello.scala,line-2")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 Add.x")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    3   LOAD_LOCAL(value x)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 *")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    3   CONSTANT(1)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @operand1")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @operand2")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#3 @operand1 @operand2 @result")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 @result")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##04")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    3   CALL_PRIMITIVE(Arithmetic(ADD,INT))
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##05")
    ?   CONSTANT("Hello.scala,line-3")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##01")
    ?   CONSTANT("NoPosition")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   RETURN(INT)

  }
  Exception handlers:

  def callAdd(): Unit {
  locals: value addResult
  startBlock: 1
  blocks: [1]

  1:
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##00 Add.callAdd class: class Add")
    ?   CONSTANT("Hello.scala,line-6")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 @this")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   THIS(Add)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 *")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   CONSTANT(8)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @this @")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   CALL_METHOD Add.add (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 Add.addResult")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   STORE_LOCAL(value addResult)
    7   SCOPE_ENTER value addResult
    7   SCOPE_EXIT value addResult
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##01")
    ?   CONSTANT("Hello.scala,line-7")
    ?   CALL_METHOD Logger.log (dynamic)
    7   RETURN(UNIT)

  }
  Exception handlers:

  def <init>(): Add {
  locals:
  startBlock: 1
  blocks: [1]

  1:
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##02")
    ?   CONSTANT("Hello.scala,line-1")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##00 Add.<init> class: class Add")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#2 @this")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    11  THIS(Add)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("#1 @javaParam1")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##06")
    ?   CONSTANT("NoPosition")
    ?   CALL_METHOD Logger.log (dynamic)
    11  CALL_METHOD java.lang.Object.<init> (super())
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##07")
    ?   CONSTANT("Hello.scala,line-11")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   LOAD_FIELD ScalaTrace.logger
    ?   CONSTANT("##01")
    ?   CONSTANT("NoPosition")
    ?   CALL_METHOD Logger.log (dynamic)
    ?   RETURN(UNIT)

  }
  Exception handlers:


