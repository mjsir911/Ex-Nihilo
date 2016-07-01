"Dynamic Variables
let dVars = {
 \"appname" : "Ex-Nihilo", 
 \"author" : name, 
 \"copyright" : "", 
 \"license" : "GPL 3.0", 
 \"version" : "0.2.0", 
 \"maintainer" : name,
 \"email" : 'msirael@gmail.com', 
 \"status" : "Prototype", 
 \"module" : ""}

"__smail__      =il.com"
"__email__
 "\"credits" : credlist, 

augroup Skeletons
 autocmd BufNewFile,BufRead *.py call g:varLoop(dVars)
augroup END
fun g:varLoop(list)
 try
  for var in keys(a:list)
   call PythonMetaUpdate(var, a:list[var])
  endfor
  catch
 endtry
endfunction
