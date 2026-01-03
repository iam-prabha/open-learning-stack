# what is YAML files ?

- YAML previously known as yet another Markup Language but now it's called (yaml ain't Markup Language) used to exchange data.
- similar to XML & JSON datatypes.
- In yaml, you can store data only for configuration and not commands.
- It is know as `Data serialisation`.
- file extension is `.yaml` or `.yml`

# Data serialisation

- object is combination of code + data like data storage unit.
- process of converting the data object that is present in some complex data structure into stream of bytes(or storage) that can be used to transfer this data on the physical devices.
- It's saves the state of the this object

object --> stream ----------> computer/databases ----------> stream --> object

serialisation                      |              Deserialization.


# where use yaml files ?

- configuration files : `Docker`, `kubernetes`, etc,.
- log, caches, etc,.

# Benefits:

- simple & easy to read
- it has strict syntax - Indentation is important.
- Easily convertable to xml and json format.
- most language uses yaml.
- more powerful represnting complex data.
- you can use various tool like parsers, etc,.

# How to validate yaml files ?

Link: 
 [blog](https://itnext.io/how-to-validate-kubernetes-yaml-files-9a17b9a30f08)
 
tool: 
  [datree](https://www.datree.io/)
  [monokie](https://github.com/kubeshop/monokle)
  [Lens](https://k8slens.dev/)
