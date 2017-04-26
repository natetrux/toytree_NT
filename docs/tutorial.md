
### Introduction

**Toytree** is a Python tree plotting library designed for use inside 
[jupyter notebooks](http://jupyter.org). In fact, this tutorial was created in a Jupyter notebook and assumes that you are following-along in a notebook of your own. Before getting started with **Toytree** it may be helpful to read some background on [**Toyplot**](http://toyplot.rtfd.io) to understand how figures are generated and displayed. If you aren’t using a notebook, you should read Toyplot's user guide section on [rendering](http://toyplot.readthedocs.io/en/stable/rendering.html#rendering) for some important information on how to display your figures.


To begin, import toyplot, toytree, and numpy. 


```python
import toytree     ## a tree plotting library
import toyplot     ## a general plotting library
import numpy       ## data generation 
```

### Toytree Class objects

Toytree has only two Python Class objects, the 
<span style="text-decoration:underline;">Toytree</span> object
that is used to represent a single tree, and the 
<span style="text-decoration:underline;">Multitree</span> object
that is used to represent a list of trees. 

To create a Toytree instance you must load in a tree representation from a newick string or file using the tree parsing function `toytree.tree`. This will parse the newick data to return a Toytree Object with the tree structure stored in memory. To do this, Toytree uses a stripped-down version of the [ete](http://etetoolkit.org) module (which we call ete3mini) for newick parsing and tree representation. Therefore, nearly all of the machinery that is available in [ete](http://etetoolkit.org) to modify and traverse trees is also available to Toytree objects. See the [Tree traversal/modification](##Tree traversal) section for more details. 

### Reading/Parsing trees
Below are two simple trees in newick format and a third in extended newick format (NHX). The first has edge lengths and support values, the second has edge-lengths and node-labels. These are two different ways of writing tree data in a serialized format. To parse either format you must tell toytree the format of the data following the [tree parsing formats in ete](http://etetoolkit.org/docs/latest/tutorial/tutorial_trees.html#reading-and-writing-newick-trees). The most commonly used format, and the default, is `format=0`. 


```python
## newick with edge-lengths & support values
newick = "((a:1,b:1)90:2,(c:3,(d:1, e:1)100:2)100:1)100;"
tre0 = toytree.tree(newick, format=0)

## newick with edge-lengths & string node-labels
newick = "((a:1,b:1)A:2,(c:3,(d:1, e:1)B:2)C:1)root;"
tre1 = toytree.tree(newick, format=1)
```

### Drawing trees (basics)


```python
## draw one tree
tre0.draw();
```


<div align="center" class="toyplot" id="t089b47821caa492b87fd08f18aa6b832"><svg class="toyplot-canvas-Canvas" height="125.0px" id="t59c1364a803e45b399cc6e986acd01c4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 125.0 125.0" width="125.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t5b8a00901d924c2aa133cf35fa2ccf46"><clipPath id="t9d1a8f5d70ce4d919239ad643ddb535e"><rect height="120.0" width="120.0" x="2.5" y="2.5"></rect></clipPath><g clip-path="url(#t9d1a8f5d70ce4d919239ad643ddb535e)"><g class="toyplot-mark-Text" id="tdb2e3becab464e5b8fdac0a133355409" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,17.857142857142861)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,40.178571428571431)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,62.5)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,84.821428571428584)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,107.14285714285714)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t54bdd8f9a9a041d7924897e66442b212"><g class="toyplot-Edges"><path d="M 12.5 54.1294642857 L 12.5 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 29.0178571429 L 64.9934383202 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 54.1294642857 L 12.5 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 79.2410714286 L 38.7467191601 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 17.8571428571 L 91.2401574803 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 40.1785714286 L 91.2401574803 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 62.5 L 91.2401574803 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 95.9821428571 L 64.9934383202 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 84.8214285714 L 91.2401574803 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 107.142857143 L 91.2401574803 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="107.14285714285714" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tb2c2ce54c7094110b7a572243a8ac6a4" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tb2c2ce54c7094110b7a572243a8ac6a4", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t089b47821caa492b87fd08f18aa6b832 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



```python
## draw multiple trees
tre0.draw();
tre1.draw();
```


<div align="center" class="toyplot" id="t1af90a48b1c64806875ecb100bb651a7"><svg class="toyplot-canvas-Canvas" height="125.0px" id="te74f7e79731448caab6cab10fa94c44a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 125.0 125.0" width="125.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tb27a26c5de38418f933607b94c571c0d"><clipPath id="t1dddf837a0be4689abc39e253531be9f"><rect height="120.0" width="120.0" x="2.5" y="2.5"></rect></clipPath><g clip-path="url(#t1dddf837a0be4689abc39e253531be9f)"><g class="toyplot-mark-Text" id="t6157471c4be143babba1056716d59dc8" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,17.857142857142861)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,40.178571428571431)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,62.5)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,84.821428571428584)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,107.14285714285714)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t917088a1564b45ddbaba727172fff378"><g class="toyplot-Edges"><path d="M 12.5 54.1294642857 L 12.5 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 29.0178571429 L 64.9934383202 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 54.1294642857 L 12.5 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 79.2410714286 L 38.7467191601 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 17.8571428571 L 91.2401574803 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 40.1785714286 L 91.2401574803 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 62.5 L 91.2401574803 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 95.9821428571 L 64.9934383202 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 84.8214285714 L 91.2401574803 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 107.142857143 L 91.2401574803 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="107.14285714285714" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tf39082b1f2104bfe8ca89eb76c8ea0a4" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tf39082b1f2104bfe8ca89eb76c8ea0a4", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t1af90a48b1c64806875ecb100bb651a7 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



<div align="center" class="toyplot" id="taaeaae108260423fa3809965da036527"><svg class="toyplot-canvas-Canvas" height="125.0px" id="t96cc201febc84f588d4c74172791e05c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 125.0 125.0" width="125.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t70c360451d38458a9ed666f75e642025"><clipPath id="tdff291dfd90144f49f966b243a0de88b"><rect height="120.0" width="120.0" x="2.5" y="2.5"></rect></clipPath><g clip-path="url(#tdff291dfd90144f49f966b243a0de88b)"><g class="toyplot-mark-Text" id="tb36d41f9f9d84148b6efc482a149c5b9" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,17.857142857142861)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,40.178571428571431)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,62.5)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,84.821428571428584)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,107.14285714285714)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="tfc70a5421e2947898e1f63127803ccaf"><g class="toyplot-Edges"><path d="M 12.5 54.1294642857 L 12.5 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 29.0178571429 L 64.9934383202 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 54.1294642857 L 12.5 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 79.2410714286 L 38.7467191601 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 17.8571428571 L 91.2401574803 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 40.1785714286 L 91.2401574803 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 62.5 L 91.2401574803 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 95.9821428571 L 64.9934383202 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 84.8214285714 L 91.2401574803 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 107.142857143 L 91.2401574803 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="107.14285714285714" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="taea12d802da745a9a0c0e20e8b8c1e95" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "taea12d802da745a9a0c0e20e8b8c1e95", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#taaeaae108260423fa3809965da036527 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



```python
## organize trees on a canvas (more on this later)
canvas = toyplot.Canvas(width=400, height=200)
ax0 = canvas.cartesian(bounds=('10%', '40%', '10%', '90%'))
ax1 = canvas.cartesian(bounds=('60%', '90%', '10%', '90%'))
tre0.draw(axes=ax0);
tre1.draw(axes=ax1);
ax0.show=False
ax1.show=False
```


<div align="center" class="toyplot" id="t6d286f01da8144cfb01dd5ab22d53ff2"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tdabb654d190a487b8e02b9573bc95927" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 200.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tdc7a9049b4e14037b4156930aef20cb3"><clipPath id="t77ece2f09c1248608c5fe9510dda370a"><rect height="180.0" width="140.0" x="30.0" y="10.0"></rect></clipPath><g clip-path="url(#t77ece2f09c1248608c5fe9510dda370a)"><g class="toyplot-mark-Text" id="t11bee5b91def4cf7b3ad75d70f260d20" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(137.95918367346937,25.581395348837219)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(137.95918367346937,62.790697674418624)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(137.95918367346937,100.00000000000001)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(137.95918367346937,137.2093023255814)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(137.95918367346937,174.41860465116281)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="tbe478ea62c9a4763b933dc6cc2d05641"><g class="toyplot-Edges"><path d="M 40.0 86.0465116279 L 40.0 44.1860465116" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 40.0 44.1860465116 L 105.306122449 44.1860465116" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 40.0 86.0465116279 L 40.0 127.906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 40.0 127.906976744 L 72.6530612245 127.906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 44.1860465116 L 105.306122449 25.5813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 25.5813953488 L 137.959183673 25.5813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 44.1860465116 L 105.306122449 62.7906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 62.7906976744 L 137.959183673 62.7906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 72.6530612245 127.906976744 L 72.6530612245 100.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 72.6530612245 100.0 L 137.959183673 100.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 72.6530612245 127.906976744 L 72.6530612245 155.813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 72.6530612245 155.813953488 L 105.306122449 155.813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 155.813953488 L 105.306122449 137.209302326" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 137.209302326 L 137.959183673 137.209302326" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 155.813953488 L 105.306122449 174.418604651" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 105.306122449 174.418604651 L 137.959183673 174.418604651" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.0" cy="86.046511627906995" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.0" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.0" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="72.65306122448979" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="72.65306122448979" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="72.65306122448979" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="72.65306122448979" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="174.41860465116281" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="174.41860465116281" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tdea4f524b2864678bf7e05f6bc80113c" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.0" cy="86.046511627906995" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="72.65306122448979" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="105.30612244897958" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="137.95918367346937" cy="174.41860465116281" r="0.0"></circle></g></g></g></g></g><g class="toyplot-coordinates-Cartesian" id="td9f211723ca14f28aeea087e150a9e4a"><clipPath id="t8312afdc74ca4ff383bd18e1cdd43692"><rect height="180.0" width="140.0" x="230.0" y="10.0"></rect></clipPath><g clip-path="url(#t8312afdc74ca4ff383bd18e1cdd43692)"><g class="toyplot-mark-Text" id="t9db26299c1204af985b46d737a079af8" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(337.9591836734694,25.581395348837219)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(337.9591836734694,62.790697674418624)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(337.9591836734694,100.00000000000001)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(337.9591836734694,137.2093023255814)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(337.9591836734694,174.41860465116281)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t984eebf082304ae9b333c298e50bcb10"><g class="toyplot-Edges"><path d="M 240.0 86.0465116279 L 240.0 44.1860465116" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 240.0 44.1860465116 L 305.306122449 44.1860465116" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 240.0 86.0465116279 L 240.0 127.906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 240.0 127.906976744 L 272.653061224 127.906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 44.1860465116 L 305.306122449 25.5813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 25.5813953488 L 337.959183673 25.5813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 44.1860465116 L 305.306122449 62.7906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 62.7906976744 L 337.959183673 62.7906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 272.653061224 127.906976744 L 272.653061224 100.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 272.653061224 100.0 L 337.959183673 100.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 272.653061224 127.906976744 L 272.653061224 155.813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 272.653061224 155.813953488 L 305.306122449 155.813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 155.813953488 L 305.306122449 137.209302326" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 137.209302326 L 337.959183673 137.209302326" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 155.813953488 L 305.306122449 174.418604651" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 305.306122449 174.418604651 L 337.959183673 174.418604651" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="86.046511627906995" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.65306122448982" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.65306122448982" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.65306122448982" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.65306122448982" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="174.41860465116281" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="174.41860465116281" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t849240ac743b473e91896c3b484c6332" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="240.0" cy="86.046511627906995" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="272.65306122448982" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="305.30612244897958" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="337.9591836734694" cy="174.41860465116281" r="0.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tdea4f524b2864678bf7e05f6bc80113c", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t849240ac743b473e91896c3b484c6332", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t6d286f01da8144cfb01dd5ab22d53ff2 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>


### The Canvas 
When you call the `toytree.draw()` function it returns two Toyplot objects which are used to display the figure. The first is the Canvas, which is the HTML element that holds the figure, and the second is a Cartesian axes object, which represent the coordinates for the plot. You can catch these objects when they are returned by the `draw()` function to further manipulate the plot. 


```python
## catch canvas and axes from draw()
canvas, axes = tre0.draw(width=200, height=250)

## e.g., turn on or off some axes elements
axes.show = True
axes.y.show = False
axes.x.ticks.show = True
```


<div align="center" class="toyplot" id="t359db455253c4cc196aa817d4e1842c8"><svg class="toyplot-canvas-Canvas" height="250.0px" id="tdec7a11b0a3c4249bfab83d193e732e8" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 200.0 250.0" width="200.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t1257c756c13b43eaa2e2de0dd14f3861"><clipPath id="tb4ffb25d949e47978fba1ef26abd96bb"><rect height="220.0" width="180.0" x="10.0" y="15.0"></rect></clipPath><g clip-path="url(#tb4ffb25d949e47978fba1ef26abd96bb)"><g class="toyplot-mark-Text" id="tfc438b83049c42a090bbd340ca8e8526" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,30.660377358490564)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,77.830188679245296)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,125.0)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,172.16981132075475)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,219.33962264150944)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="tfbe45249855e4e2091f8f30251bd9103"><g class="toyplot-Edges"><path d="M 20.0 107.311320755 L 20.0 54.2452830189" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 20.0 54.2452830189 L 111.265597148 54.2452830189" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 20.0 107.311320755 L 20.0 160.377358491" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 20.0 160.377358491 L 65.632798574 160.377358491" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 54.2452830189 L 111.265597148 30.6603773585" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 30.6603773585 L 156.898395722 30.6603773585" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 54.2452830189 L 111.265597148 77.8301886792" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 77.8301886792 L 156.898395722 77.8301886792" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 160.377358491 L 65.632798574 125.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 125.0 L 156.898395722 125.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 160.377358491 L 65.632798574 195.754716981" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 195.754716981 L 111.265597148 195.754716981" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 195.754716981 L 111.265597148 172.169811321" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 172.169811321 L 156.898395722 172.169811321" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 195.754716981 L 111.265597148 219.339622642" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 219.339622642 L 156.898395722 219.339622642" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="107.31132075471699" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="54.245283018867923" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="54.245283018867923" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="160.37735849056602" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="160.37735849056602" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="54.245283018867923" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="30.660377358490564" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="30.660377358490564" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="77.830188679245296" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="77.830188679245296" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="160.37735849056602" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="125.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="125.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="195.75471698113208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="195.75471698113208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="195.75471698113208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="172.16981132075475" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="172.16981132075475" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="219.33962264150944" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="219.33962264150944" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t108f95836b8747e0b75c5d57e9d3348d" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="107.31132075471699" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="54.245283018867923" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="160.37735849056602" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="195.75471698113208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="30.660377358490564" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="77.830188679245296" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="125.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="172.16981132075475" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="219.33962264150944" r="0.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t90bcd5dac59c4c5ab44462a2707725e3" transform="translate(20.0,225.0)translate(0,10.0)"><line style="" x1="0" x2="136.89839572192514" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="0" y2="-5"></line><line style="" x1="45.632798573975045" x2="45.632798573975045" y1="0" y2="-5"></line><line style="" x1="91.26559714795009" x2="91.26559714795009" y1="0" y2="-5"></line><line style="" x1="136.89839572192514" x2="136.89839572192514" y1="0" y2="-5"></line></g><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">-3</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(45.632798573975045,6)translate(0,7.5)"><tspan style="font-size:10.0px">-2</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(91.26559714795009,6)translate(0,7.5)"><tspan style="font-size:10.0px">-1</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(136.89839572192514,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t108f95836b8747e0b75c5d57e9d3348d", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t359db455253c4cc196aa817d4e1842c8 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script><script>
        (function()
        {
            function _sign(x)
            {
                return x < 0 ? -1 : x > 0 ? 1 : 0;
            }

            function _mix(a, b, amount)
            {
                return ((1.0 - amount) * a) + (amount * b);
            }

            function _log(x, base)
            {
                return Math.log(Math.abs(x)) / Math.log(base);
            }

            function _in_range(a, x, b)
            {
                var left = Math.min(a, b);
                var right = Math.max(a, b);
                return left <= x && x <= right;
            }

            function inside(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(_in_range(segment.range.min, range, segment.range.max))
                        return true;
                }
                return false;
            }

            function to_domain(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                    {
                        if(segment.scale == "linear")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            return _mix(segment.domain.min, segment.domain.max, amount)
                        }
                        else if(segment.scale[0] == "log")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            var base = segment.scale[1];
                            return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                        }
                    }
                }
            }

            function display_coordinates(e)
            {
                var current = svg.createSVGPoint();
                current.x = e.clientX;
                current.y = e.clientY;

                for(var axis_id in axes)
                {
                    var axis = document.querySelector("#" + axis_id);
                    var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                    if(coordinates)
                    {
                        var projection = axes[axis_id];
                        var local = current.matrixTransform(axis.getScreenCTM().inverse());
                        if(inside(local.x, projection))
                        {
                            var domain = to_domain(local.x, projection);
                            coordinates.style.visibility = "visible";
                            coordinates.setAttribute("transform", "translate(" + local.x + ")");
                            var text = coordinates.querySelector("text");
                            text.textContent = domain.toFixed(2);
                        }
                        else
                        {
                            coordinates.style.visibility= "hidden";
                        }
                    }
                }
            }

            var root_id = "t359db455253c4cc196aa817d4e1842c8";
            var axes = {"t90bcd5dac59c4c5ab44462a2707725e3": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5062499999999999, "min": -3.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 160.0, "min": 0.0}, "scale": "linear"}]};

            var svg = document.querySelector("#" + root_id + " svg");
            svg.addEventListener("click", display_coordinates);
        })();
        </script></div></div>


Or, instead of catching the canvas and axes auto-generated by the `toytree.draw()` function you can instead generate the canvas and axes yourself using Toyplot and embed the tree plot in the canvas. 


```python
## create the canvas 
canvas = toyplot.Canvas(width=250, height=250)
axes = canvas.cartesian(gutter=50)

## add tree to existing canvas
canvas, axes = tre0.draw(axes=axes)

## further modify the axes
axes.y.show = False
axes.x.ticks.show = True
axes.x.label.text = "Divergence time (Ma)"
```


<div align="center" class="toyplot" id="t1031cd4e61a04cd48f594820b48e5fa4"><svg class="toyplot-canvas-Canvas" height="250.0px" id="t04b5e02a3df84be5abd22e5abb842f63" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 250.0 250.0" width="250.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t23726ba4a0d3405ebdd4bedae7d9d909"><clipPath id="tf95b8e54890142ba8ddd5bb396fae33e"><rect height="170.0" width="170.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tf95b8e54890142ba8ddd5bb396fae33e)"><g class="toyplot-mark-Text" id="teb669d537d7f476e95ef8430ef674dc2" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(177.11864406779659,55.555555555555564)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(177.11864406779659,90.277777777777771)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(177.11864406779659,125.0)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(177.11864406779659,159.72222222222223)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(177.11864406779659,194.44444444444446)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="ta032d2cb9e634651bfa3df292c83cb39"><g class="toyplot-Edges"><path d="M 50.0 111.979166667 L 50.0 72.9166666667" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 50.0 72.9166666667 L 134.745762712 72.9166666667" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 50.0 111.979166667 L 50.0 151.041666667" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 50.0 151.041666667 L 92.3728813559 151.041666667" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 72.9166666667 L 134.745762712 55.5555555556" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 55.5555555556 L 177.118644068 55.5555555556" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 72.9166666667 L 134.745762712 90.2777777778" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 90.2777777778 L 177.118644068 90.2777777778" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 92.3728813559 151.041666667 L 92.3728813559 125.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 92.3728813559 125.0 L 177.118644068 125.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 92.3728813559 151.041666667 L 92.3728813559 177.083333333" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 92.3728813559 177.083333333 L 134.745762712 177.083333333" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 177.083333333 L 134.745762712 159.722222222" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 159.722222222 L 177.118644068 159.722222222" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 177.083333333 L 134.745762712 194.444444444" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 134.745762712 194.444444444 L 177.118644068 194.444444444" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="111.97916666666666" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="72.916666666666657" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="72.916666666666657" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="151.04166666666669" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="92.372881355932208" cy="151.04166666666669" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="72.916666666666657" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="55.555555555555564" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="55.555555555555564" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="90.277777777777771" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="90.277777777777771" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="92.372881355932208" cy="151.04166666666669" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="92.372881355932208" cy="125.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="125.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="92.372881355932208" cy="177.08333333333331" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="177.08333333333331" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="177.08333333333331" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="159.72222222222223" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="159.72222222222223" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="194.44444444444446" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="194.44444444444446" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tec1fa575fdca4e0197ab11e324634707" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="50.0" cy="111.97916666666666" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="72.916666666666657" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="92.372881355932208" cy="151.04166666666669" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="134.74576271186442" cy="177.08333333333331" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="55.555555555555564" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="90.277777777777771" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="125.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="159.72222222222223" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="177.11864406779659" cy="194.44444444444446" r="0.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t1b2e04c9420e45b0a71291bc02e5e9b2" transform="translate(50.0,200.0)translate(0,10.0)"><line style="" x1="0" x2="127.11864406779661" y1="0" y2="0"></line><g><line style="" x1="0.0" x2="0.0" y1="0" y2="-5"></line><line style="" x1="42.37288135593221" x2="42.37288135593221" y1="0" y2="-5"></line><line style="" x1="84.74576271186442" x2="84.74576271186442" y1="0" y2="-5"></line><line style="" x1="127.11864406779661" x2="127.11864406779661" y1="0" y2="-5"></line></g><g><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(0.0,6)translate(0,7.5)"><tspan style="font-size:10.0px">-3</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(42.37288135593221,6)translate(0,7.5)"><tspan style="font-size:10.0px">-2</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(84.74576271186442,6)translate(0,7.5)"><tspan style="font-size:10.0px">-1</tspan></text><text style="font-weight:normal;stroke:none;text-anchor:middle" transform="translate(127.11864406779661,6)translate(0,7.5)"><tspan style="font-size:10.0px">0</tspan></text></g><text style="font-weight:bold;stroke:none;text-anchor:middle" transform="translate(75.0,22)translate(0,9.0)"><tspan style="font-size:12.0px">Divergence time (Ma)</tspan></text><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tec1fa575fdca4e0197ab11e324634707", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t1031cd4e61a04cd48f594820b48e5fa4 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script><script>
        (function()
        {
            function _sign(x)
            {
                return x < 0 ? -1 : x > 0 ? 1 : 0;
            }

            function _mix(a, b, amount)
            {
                return ((1.0 - amount) * a) + (amount * b);
            }

            function _log(x, base)
            {
                return Math.log(Math.abs(x)) / Math.log(base);
            }

            function _in_range(a, x, b)
            {
                var left = Math.min(a, b);
                var right = Math.max(a, b);
                return left <= x && x <= right;
            }

            function inside(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(_in_range(segment.range.min, range, segment.range.max))
                        return true;
                }
                return false;
            }

            function to_domain(range, projection)
            {
                for(var i = 0; i != projection.length; ++i)
                {
                    var segment = projection[i];
                    if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                    {
                        if(segment.scale == "linear")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            return _mix(segment.domain.min, segment.domain.max, amount)
                        }
                        else if(segment.scale[0] == "log")
                        {
                            var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                            var base = segment.scale[1];
                            return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                        }
                    }
                }
            }

            function display_coordinates(e)
            {
                var current = svg.createSVGPoint();
                current.x = e.clientX;
                current.y = e.clientY;

                for(var axis_id in axes)
                {
                    var axis = document.querySelector("#" + axis_id);
                    var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                    if(coordinates)
                    {
                        var projection = axes[axis_id];
                        var local = current.matrixTransform(axis.getScreenCTM().inverse());
                        if(inside(local.x, projection))
                        {
                            var domain = to_domain(local.x, projection);
                            coordinates.style.visibility = "visible";
                            coordinates.setAttribute("transform", "translate(" + local.x + ")");
                            var text = coordinates.querySelector("text");
                            text.textContent = domain.toFixed(2);
                        }
                        else
                        {
                            coordinates.style.visibility= "hidden";
                        }
                    }
                }
            }

            var root_id = "t1031cd4e61a04cd48f594820b48e5fa4";
            var axes = {"t1b2e04c9420e45b0a71291bc02e5e9b2": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 0.5399999999999998, "min": -3.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0.0}, "scale": "linear"}]};

            var svg = document.querySelector("#" + root_id + " svg");
            svg.addEventListener("click", display_coordinates);
        })();
        </script></div></div>


### Drawing trees (advanced)
See the sections on [node-labels](node-labels.md) and [tip-labels](tip-labels.md) for detailed instructions on how to modify these features. Here I will concentrate on how Toytree works to ensure that users display the proper data on the tree and avoid mistakes. First off, we provide the *magic command* `node_labels=True` which embeds interactive features into the plot so that if you hover over any node with your cursor you can see all of the information available for that node that is extracted from the tree.  


```python
## 'False' blocks node labels
canvas, axes = tre0.draw(
    width=150,
    node_labels=False,
    )

## But, you can still change size and color of nodes
canvas, axes = tre0.draw(
    width=150,
    node_labels=False,
    node_size=12,
    node_color='grey'
    )

## 'True' shows nodes with interactive information when you hover
canvas, axes = tre0.draw(
    width=150,
    node_labels=True,
    node_size=12
    )
```


<div align="center" class="toyplot" id="t9e29f34c5e524096b076a573759f8bde"><svg class="toyplot-canvas-Canvas" height="150.0px" id="t8a6e72b0e2e4473d9ab4fdaeb4c4a355" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 150.0 150.0" width="150.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t775c6d0be5114365858294a19546e33e"><clipPath id="t5c776a010c6249968d5f950ffba9447d"><rect height="140.0" width="140.0" x="5.0" y="5.0"></rect></clipPath><g clip-path="url(#t5c776a010c6249968d5f950ffba9447d)"><g class="toyplot-mark-Text" id="t5682ab92ec7749e4b0e23cae3daa09fd" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,20.45454545454546)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,47.72727272727272)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,75.0)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,102.27272727272728)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,129.54545454545456)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t61d94cd5d637405bb0f4a390b9ba58f7"><g class="toyplot-Edges"><path d="M 15.0 64.7727272727 L 15.0 34.0909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 34.0909090909 L 80.306122449 34.0909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 64.7727272727 L 15.0 95.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 95.4545454545 L 47.6530612245 95.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 34.0909090909 L 80.306122449 20.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 20.4545454545 L 112.959183673 20.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 34.0909090909 L 80.306122449 47.7272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 47.7272727273 L 112.959183673 47.7272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 95.4545454545 L 47.6530612245 75.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 75.0 L 112.959183673 75.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 95.4545454545 L 47.6530612245 115.909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 115.909090909 L 80.306122449 115.909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 115.909090909 L 80.306122449 102.272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 102.272727273 L 112.959183673 102.272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 115.909090909 L 80.306122449 129.545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 129.545454545 L 112.959183673 129.545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="64.77272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="129.54545454545456" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="129.54545454545456" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t32a32f4a09424c8b928fa6f4cbb73058" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="64.77272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="129.54545454545456" r="0.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t32a32f4a09424c8b928fa6f4cbb73058", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t9e29f34c5e524096b076a573759f8bde .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



<div align="center" class="toyplot" id="t0d0fc86e7f6c49f48b36478afc869302"><svg class="toyplot-canvas-Canvas" height="150.0px" id="tc948b3243b9340669232104ec98a504f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 150.0 150.0" width="150.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tbdaca647cfd24e32ba970cad477590da"><clipPath id="t6ad3c9600996430b8685b7e821163655"><rect height="140.0" width="140.0" x="5.0" y="5.0"></rect></clipPath><g clip-path="url(#t6ad3c9600996430b8685b7e821163655)"><g class="toyplot-mark-Text" id="tf5f523592a5a4168a07d70bcc8a01466" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,20.45454545454546)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,47.72727272727272)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,75.0)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,102.27272727272728)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,129.54545454545456)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="tf077229adbb74e899b7493ea9f4af6bc"><g class="toyplot-Edges"><path d="M 15.0 64.7727272727 L 15.0 34.0909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 34.0909090909 L 80.306122449 34.0909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 64.7727272727 L 15.0 95.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 95.4545454545 L 47.6530612245 95.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 34.0909090909 L 80.306122449 20.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 20.4545454545 L 112.959183673 20.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 34.0909090909 L 80.306122449 47.7272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 47.7272727273 L 112.959183673 47.7272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 95.4545454545 L 47.6530612245 75.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 75.0 L 112.959183673 75.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 95.4545454545 L 47.6530612245 115.909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 115.909090909 L 80.306122449 115.909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 115.909090909 L 80.306122449 102.272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 102.272727273 L 112.959183673 102.272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 115.909090909 L 80.306122449 129.545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 129.545454545 L 112.959183673 129.545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="64.77272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="129.54545454545456" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="129.54545454545456" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t5c829fc472654901a3f56c96cc183187" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="64.77272727272728" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="20.45454545454546" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="47.72727272727272" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="75.0" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="102.27272727272728" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.2%,50.2%,50.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="129.54545454545456" r="6.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t5c829fc472654901a3f56c96cc183187", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#t0d0fc86e7f6c49f48b36478afc869302 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



<div align="center" class="toyplot" id="tccd3ce55df164bc784d698eced8951f7"><svg class="toyplot-canvas-Canvas" height="150.0px" id="te3a7da5c1462405a85c0b423003bcb99" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 150.0 150.0" width="150.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t28cc9c9a6fd643fc935a4825e0e83bef"><clipPath id="tad70e3ffe3db433b97a3f728271c1e26"><rect height="140.0" width="140.0" x="5.0" y="5.0"></rect></clipPath><g clip-path="url(#tad70e3ffe3db433b97a3f728271c1e26)"><g class="toyplot-mark-Text" id="t9be630a9073c4517a11e3b37dce8696e" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,20.45454545454546)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,47.72727272727272)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,75.0)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,102.27272727272728)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(112.95918367346937,129.54545454545456)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t895bd04a9f3e4f97a2c89b2e06ccf3e2"><g class="toyplot-Edges"><path d="M 15.0 64.7727272727 L 15.0 34.0909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 34.0909090909 L 80.306122449 34.0909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 64.7727272727 L 15.0 95.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.0 95.4545454545 L 47.6530612245 95.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 34.0909090909 L 80.306122449 20.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 20.4545454545 L 112.959183673 20.4545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 34.0909090909 L 80.306122449 47.7272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 47.7272727273 L 112.959183673 47.7272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 95.4545454545 L 47.6530612245 75.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 75.0 L 112.959183673 75.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 95.4545454545 L 47.6530612245 115.909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 47.6530612245 115.909090909 L 80.306122449 115.909090909" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 115.909090909 L 80.306122449 102.272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 102.272727273 L 112.959183673 102.272727273" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 115.909090909 L 80.306122449 129.545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 80.306122449 129.545454545 L 112.959183673 129.545454545" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="64.77272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.0" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="34.090909090909101" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="20.45454545454546" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="47.72727272727272" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="95.454545454545439" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="75.0" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="47.65306122448979" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="115.90909090909092" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="102.27272727272728" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="80.306122448979579" cy="129.54545454545456" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.95918367346937" cy="129.54545454545456" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t49a5c83f3d7243cba04a704f6d018f3d" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 0
name: 0
dist: 0
support: 100</title><circle cx="15.0" cy="64.77272727272728" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 1
name: 1
dist: 2
support: 90</title><circle cx="80.306122448979579" cy="34.090909090909101" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 2
name: 2
dist: 1
support: 100</title><circle cx="47.65306122448979" cy="95.454545454545439" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 3
name: 3
dist: 2
support: 100</title><circle cx="80.306122448979579" cy="115.90909090909092" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 4
name: a
dist: 1
support: 100</title><circle cx="112.95918367346937" cy="20.45454545454546" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 5
name: b
dist: 1
support: 100</title><circle cx="112.95918367346937" cy="47.72727272727272" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 6
name: c
dist: 3
support: 100</title><circle cx="112.95918367346937" cy="75.0" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 7
name: d
dist: 1
support: 100</title><circle cx="112.95918367346937" cy="102.27272727272728" r="6.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><title>idx: 8
name: e
dist: 1
support: 100</title><circle cx="112.95918367346937" cy="129.54545454545456" r="6.0"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t49a5c83f3d7243cba04a704f6d018f3d", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#tccd3ce55df164bc784d698eced8951f7 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>


### Extracting data from the tree

Although you *can* enter values for the node_labels or tip_labels directly into the draw() function as a list, doing so is frowned upon because it can often lead to errors if the values are entered in the incorrect order, or if the tree is re-oriented, ladderized, or pruned. Instead, Toytree aims to encourage users to *always* extract the data directly from the Tree object itself, such that the data will always be in sync with the tree. The interactive feature `node_label=True` is one example of this, where all of the information for each node is shown, and extracted from the tree, so you know for sure that the data are in sync. 

In addition, we provide convenience functions to extract data from a Toytree object in the order that it will be plotted on the tree. For node values the function `get_node_values()` should be used, and for tip labels the function `get_tip_labels()` should be used. Below we show some example usage of `get_node_values()`. See the section on [node-labels](node-labels.md) and [modifying the tree object](modifying-the-tree.md) for more information. 


```python
## get node values returns a list of values, empty by default
tre0.get_node_values()
```




    ['', ' ', ' ', ' ', '', '', '', '', '']




```python
## it takes up to three arguments
tre0.get_node_values(feature='idx', show_root=False, show_tips=False)
```




    ['', 1, 2, 3, '', '', '', '', '']




```python
## it can access any feature in the tree 
tre0.get_node_values(feature='name', show_root=False, show_tips=False)
```




    ['', '1', '2', '3', '', '', '', '', '']




```python
## and either hide or show the root & tip values
tre0.get_node_values(feature='name', show_root=True, show_tips=True)
```




    ['0', '1', '2', '3', 'a', 'b', 'c', 'd', 'e']




```python
## show the index number (idx) of each node
tre0.draw(node_labels=tre0.get_node_values("idx", True, True));
```


<div align="center" class="toyplot" id="tf589fd99e9864bb0af4e924a23572cb9"><svg class="toyplot-canvas-Canvas" height="125.0px" id="t61e6869ff5e742e793dc32a1879d8249" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 125.0 125.0" width="125.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="td991e57923ff43b5b56ac2d1dba572e7"><clipPath id="t7a5cd7e8ade941c383f0c30dbac35852"><rect height="120.0" width="120.0" x="2.5" y="2.5"></rect></clipPath><g clip-path="url(#t7a5cd7e8ade941c383f0c30dbac35852)"><g class="toyplot-mark-Text" id="td5f15a371fce45faa107ce76276137ab" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,17.857142857142861)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,40.178571428571431)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,62.5)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,84.821428571428584)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,107.14285714285714)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t3289932180f04af28db233f756545dcc"><g class="toyplot-Edges"><path d="M 15.9220532319 54.1294642857 L 15.9220532319 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.9220532319 29.0178571429 L 66.6191381496 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.9220532319 54.1294642857 L 15.9220532319 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.9220532319 79.2410714286 L 41.2705956907 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 29.0178571429 L 66.6191381496 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 17.8571428571 L 91.9676806084 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 29.0178571429 L 66.6191381496 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 40.1785714286 L 91.9676806084 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 79.2410714286 L 41.2705956907 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 62.5 L 91.9676806084 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 79.2410714286 L 41.2705956907 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 95.9821428571 L 66.6191381496 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 95.9821428571 L 66.6191381496 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 84.8214285714 L 91.9676806084 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 95.9821428571 L 66.6191381496 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 107.142857143 L 91.9676806084 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="107.14285714285714" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t26d9377f356c4c6ba0779ec1727de3f6" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="54.129464285714292" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="29.017857142857153" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="79.241071428571431" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="95.982142857142861" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="17.857142857142861" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="40.178571428571431" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="62.5" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="84.821428571428584" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="107.14285714285714" r="7.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tffcbdbf19a054a34bcd4a28849fba47a" style="alignment-baseline:middle;fill:262626;font-size:9px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(15.922053231939158,54.129464285714292)translate(0,2.53125)"><tspan style="font-size:9.0px">0</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(66.619138149556406,29.017857142857153)translate(0,2.53125)"><tspan style="font-size:9.0px">1</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(41.270595690747783,79.241071428571431)translate(0,2.53125)"><tspan style="font-size:9.0px">2</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(66.619138149556406,95.982142857142861)translate(0,2.53125)"><tspan style="font-size:9.0px">3</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,17.857142857142861)translate(0,2.53125)"><tspan style="font-size:9.0px">4</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,40.178571428571431)translate(0,2.53125)"><tspan style="font-size:9.0px">5</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,62.5)translate(0,2.53125)"><tspan style="font-size:9.0px">6</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,84.821428571428584)translate(0,2.53125)"><tspan style="font-size:9.0px">7</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,107.14285714285714)translate(0,2.53125)"><tspan style="font-size:9.0px">8</tspan></text></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t26d9377f356c4c6ba0779ec1727de3f6", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#tf589fd99e9864bb0af4e924a23572cb9 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



```python
## show names (if no internal names then idx is shown)
tre0.draw(node_labels=tre0.get_node_values("name", True, True));
```


<div align="center" class="toyplot" id="td8ac3933907c4a7bb7fcefecc52c66d4"><svg class="toyplot-canvas-Canvas" height="125.0px" id="t4806508e2cb5448498ad7fd6e4a2857d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 125.0 125.0" width="125.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tdf59305f921e466e8a3b736fa076e72d"><clipPath id="ta178582e2dde4478bde2362e9f05c7c6"><rect height="120.0" width="120.0" x="2.5" y="2.5"></rect></clipPath><g clip-path="url(#ta178582e2dde4478bde2362e9f05c7c6)"><g class="toyplot-mark-Text" id="t2e72a72132ca4f22abe2010e3c7cfa88" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,17.857142857142861)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,40.178571428571431)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,62.5)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,84.821428571428584)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.967680608365015,107.14285714285714)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t2db444d541624709ae5a19f22e1ede67"><g class="toyplot-Edges"><path d="M 15.9220532319 54.1294642857 L 15.9220532319 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.9220532319 29.0178571429 L 66.6191381496 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.9220532319 54.1294642857 L 15.9220532319 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 15.9220532319 79.2410714286 L 41.2705956907 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 29.0178571429 L 66.6191381496 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 17.8571428571 L 91.9676806084 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 29.0178571429 L 66.6191381496 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 40.1785714286 L 91.9676806084 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 79.2410714286 L 41.2705956907 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 62.5 L 91.9676806084 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 79.2410714286 L 41.2705956907 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 41.2705956907 95.9821428571 L 66.6191381496 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 95.9821428571 L 66.6191381496 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 84.8214285714 L 91.9676806084 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 95.9821428571 L 66.6191381496 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 66.6191381496 107.142857143 L 91.9676806084 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="107.14285714285714" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t7b34278876774c19bcf70ac206eaf618" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="15.922053231939158" cy="54.129464285714292" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="29.017857142857153" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="41.270595690747783" cy="79.241071428571431" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="66.619138149556406" cy="95.982142857142861" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="17.857142857142861" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="40.178571428571431" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="62.5" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="84.821428571428584" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.967680608365015" cy="107.14285714285714" r="7.5"></circle></g></g></g><g class="toyplot-mark-Text" id="tba5bc106899e498590971f7bfcf872e2" style="alignment-baseline:middle;fill:262626;font-size:9px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(15.922053231939158,54.129464285714292)translate(0,2.53125)"><tspan style="font-size:9.0px">0</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(66.619138149556406,29.017857142857153)translate(0,2.53125)"><tspan style="font-size:9.0px">1</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(41.270595690747783,79.241071428571431)translate(0,2.53125)"><tspan style="font-size:9.0px">2</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(66.619138149556406,95.982142857142861)translate(0,2.53125)"><tspan style="font-size:9.0px">3</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,17.857142857142861)translate(0,2.53125)"><tspan style="font-size:9.0px">a</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,40.178571428571431)translate(0,2.53125)"><tspan style="font-size:9.0px">b</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,62.5)translate(0,2.53125)"><tspan style="font-size:9.0px">c</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,84.821428571428584)translate(0,2.53125)"><tspan style="font-size:9.0px">d</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(91.967680608365015,107.14285714285714)translate(0,2.53125)"><tspan style="font-size:9.0px">e</tspan></text></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "t7b34278876774c19bcf70ac206eaf618", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#td8ac3933907c4a7bb7fcefecc52c66d4 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



```python
## show support values (hides root & tip values by default)
tre0.draw(node_labels=tre0.get_node_values("support"));
```


<div align="center" class="toyplot" id="tccfadb7821c244a78608d069be556d35"><svg class="toyplot-canvas-Canvas" height="125.0px" id="td2a45b08e1b844f8824317853bb5a44a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 125.0 125.0" width="125.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t0ddfc9b128ad422297e21575aa0e8fba"><clipPath id="t47470bf617fa40fd8a63cc561c5f37ff"><rect height="120.0" width="120.0" x="2.5" y="2.5"></rect></clipPath><g clip-path="url(#t47470bf617fa40fd8a63cc561c5f37ff)"><g class="toyplot-mark-Text" id="t818994ca2cbc45dcb197fd26c696294d" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,17.857142857142861)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,40.178571428571431)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,62.5)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,84.821428571428584)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(91.240157480314963,107.14285714285714)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="tf62479afb07345a387c285a4365cf238"><g class="toyplot-Edges"><path d="M 12.5 54.1294642857 L 12.5 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 29.0178571429 L 64.9934383202 29.0178571429" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 54.1294642857 L 12.5 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 12.5 79.2410714286 L 38.7467191601 79.2410714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 17.8571428571 L 91.2401574803 17.8571428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 29.0178571429 L 64.9934383202 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 40.1785714286 L 91.2401574803 40.1785714286" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 62.5 L 91.2401574803 62.5" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 79.2410714286 L 38.7467191601 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 38.7467191601 95.9821428571 L 64.9934383202 95.9821428571" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 84.8214285714 L 91.2401574803 84.8214285714" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 95.9821428571 L 64.9934383202 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 64.9934383202 107.142857143 L 91.2401574803 107.142857143" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="107.14285714285714" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tee9d0ec1d0524e43914ef4ffe9fc3b46" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="12.5" cy="54.129464285714292" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="29.017857142857153" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="38.746719160104988" cy="79.241071428571431" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="64.993438320209975" cy="95.982142857142861" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="17.857142857142861" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="40.178571428571431" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="62.5" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="84.821428571428584" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.240157480314963" cy="107.14285714285714" r="0.0"></circle></g></g></g><g class="toyplot-mark-Text" id="tc281ee3c4e3747bf91fa4e5c24b80383" style="alignment-baseline:middle;fill:262626;font-size:9px;font-weight:normal;stroke:none;text-anchor:middle"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(64.993438320209975,29.017857142857153)translate(0,2.53125)"><tspan style="font-size:9.0px">90</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(38.746719160104988,79.241071428571431)translate(0,2.53125)"><tspan style="font-size:9.0px">100</tspan></text><text class="toyplot-Datum" style="fill:262626;font-weight:normal;opacity:1.0;stroke:none;text-anchor:middle" transform="translate(64.993438320209975,95.982142857142861)translate(0,2.53125)"><tspan style="font-size:9.0px">100</tspan></text></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tee9d0ec1d0524e43914ef4ffe9fc3b46", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#tccfadb7821c244a78608d069be556d35 .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>



```python
## parse the info and plot as node_size
colors = [tre0.colors[0] if i==100 else tre0.colors[1] \
          for i in tre0.get_node_values("support", True, True)]

## plot node colors and hide stroke color
tre0.draw(
    width=200,
    node_labels=False, 
    node_color=colors,
    node_size=15,
    node_style={"stroke": 'none'}
);
```


<div align="center" class="toyplot" id="tb444cf6ea1a04cafa0fce1241cd21dde"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t4fd851b527084d90af0d87b6270c073e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 200.0 200.0" width="200.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t636db87798fd456baf53f6f4e3020150"><clipPath id="te60c99cb13a642dea61d9dd442ffd679"><rect height="180.0" width="180.0" x="10.0" y="10.0"></rect></clipPath><g clip-path="url(#te60c99cb13a642dea61d9dd442ffd679)"><g class="toyplot-mark-Text" id="te6b7451a091c4b6cb7ce2df3efc91046" style="-toyplot-anchor-shift:15px;alignment-baseline:middle;font-size:12px;font-weight:normal;stroke:none;text-anchor:start"><g class="toyplot-Series"><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,25.581395348837219)translate(15.0,3.375)"><tspan style="font-size:12.0px">a</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,62.790697674418624)translate(15.0,3.375)"><tspan style="font-size:12.0px">b</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,100.00000000000001)translate(15.0,3.375)"><tspan style="font-size:12.0px">c</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,137.2093023255814)translate(15.0,3.375)"><tspan style="font-size:12.0px">d</tspan></text><text class="toyplot-Datum" style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-weight:normal;opacity:1.0;stroke:none;text-anchor:start" transform="translate(156.89839572192514,174.41860465116281)translate(15.0,3.375)"><tspan style="font-size:12.0px">e</tspan></text></g></g><g class="toyplot-mark-Graph" id="t946f3e3d3dc64708a8d0b057a26425e8"><g class="toyplot-Edges"><path d="M 20.0 86.0465116279 L 20.0 44.1860465116" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 20.0 44.1860465116 L 111.265597148 44.1860465116" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 20.0 86.0465116279 L 20.0 127.906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 20.0 127.906976744 L 65.632798574 127.906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 44.1860465116 L 111.265597148 25.5813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 25.5813953488 L 156.898395722 25.5813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 44.1860465116 L 111.265597148 62.7906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 62.7906976744 L 156.898395722 62.7906976744" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 127.906976744 L 65.632798574 100.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 100.0 L 156.898395722 100.0" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 127.906976744 L 65.632798574 155.813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 65.632798574 155.813953488 L 111.265597148 155.813953488" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 155.813953488 L 111.265597148 137.209302326" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 137.209302326 L 156.898395722 137.209302326" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 155.813953488 L 111.265597148 174.418604651" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path><path d="M 111.265597148 174.418604651 L 156.898395722 174.418604651" style="fill:none;stroke:rgb(16.1%,15.3%,14.1%);stroke-linecap:round;stroke-opacity:1.0;stroke-width:2"></path></g><g class="toyplot-Vertices"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="86.046511627906995" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.0" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="44.186046511627936" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="25.581395348837219" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="62.790697674418624" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="127.90697674418605" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="100.00000000000001" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="65.632798573975037" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="155.81395348837208" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="137.2093023255814" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="111.26559714795009" cy="174.41860465116281" r="0.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="156.89839572192514" cy="174.41860465116281" r="0.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tcc120b9bf34e43abbd51a528efda6eb7" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="20.0" cy="86.046511627906995" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="111.26559714795009" cy="44.186046511627936" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="65.632798573975037" cy="127.90697674418605" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="111.26559714795009" cy="155.81395348837208" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="156.89839572192514" cy="25.581395348837219" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="156.89839572192514" cy="62.790697674418624" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="156.89839572192514" cy="100.00000000000001" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="156.89839572192514" cy="137.2093023255814" r="7.5"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:none"><circle cx="156.89839572192514" cy="174.41860465116281" r="7.5"></circle></g></g></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
            <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
            <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                Save as .csv
            </li>
        </ul><script>
        (function()
        {
          var data_tables = [{"title": "Scatterplot Data", "names": ["x", "y0"], "id": "tcc120b9bf34e43abbd51a528efda6eb7", "columns": [[-3.0, -1.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [2.375, 3.5, 1.25, 0.5, 4.0, 3.0, 2.0, 1.0, 0.0]], "filename": "toyplot"}];

          function save_csv(data_table)
          {
            var uri = "data:text/csv;charset=utf-8,";
            uri += data_table.names.join(",") + "\n";
            for(var i = 0; i != data_table.columns[0].length; ++i)
            {
              for(var j = 0; j != data_table.columns.length; ++j)
              {
                if(j)
                  uri += ",";
                uri += data_table.columns[j][i];
              }
              uri += "\n";
            }
            uri = encodeURI(uri);

            var link = document.createElement("a");
            if(typeof link.download != "undefined")
            {
              link.href = uri;
              link.style = "visibility:hidden";
              link.download = data_table.filename + ".csv";

              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            else
            {
              window.open(uri);
            }
          }

          function open_popup(data_table)
          {
            return function(e)
            {
              var popup = document.querySelector("#tb444cf6ea1a04cafa0fce1241cd21dde .toyplot-mark-popup");
              popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
              popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
              popup.style.left = (e.clientX - 50) + "px";
              popup.style.top = (e.clientY - 20) + "px";
              popup.style.visibility = "visible";
              e.stopPropagation();
              e.preventDefault();
            }

          }

          for(var i = 0; i != data_tables.length; ++i)
          {
            var data_table = data_tables[i];
            var event_target = document.querySelector("#" + data_table.id);
            event_target.oncontextmenu = open_popup(data_table);
          }
        })();
        </script></div></div>
