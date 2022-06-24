module MatMultCAMsg
{
  use ServerConfig;
  use MultiTypeSymEntry;
  use ServerErrorStrings;
  use MultiTypeSymbolTable;

  // do foo on array a
  proc MatMultCommAvoiding(a: [?aD] int): [aD] int {
    //...
    return(ret);
  }

  /*
  Parse, execute, and respond to a foo message
  :arg reqMsg: request containing (cmd,dtype,size)
  :type reqMsg: string
  :arg st: SymTab to act on
  :type st: borrowed SymTab
  :returns: (string) response message
  */

  proc MatMultCommAvoidingMsg(reqMsg: string, st: borrowed SymTab): string throws {

    var repMsg: string; // response message

    // split request into fields
    var (cmd, name) = reqMsg.splitMsgToTuple(2);

    // get next symbol name
    var rname = st.nextName();

    var gEnt: borrowed GenSymEntry = st.lookup(name);

    if (gEnt == nil) {return unknownSymbolError("set",name);}

    // if verbose print action
    if v {try! writeln("%s %s: %s".format(cmd,name,rname)); try! stdout.flush();}

    select (gEnt.dtype) {
        when (DType.Int64) {
            var e = toSymEntry(gEnt,int);
            var ret = foo(e.a);
            st.addEntry(rname, new shared SymEntry(ret));
        }
        otherwise {return notImplementedError("foo",gEnt.dtype);}
    }

    // response message
    return try! "created " + st.attrib(rname);
  }


  proc registerMe() {
    use CommandMap;
    registerFunction("MatMultCommAvoiding", MatMultCAMsg);
  }
}
