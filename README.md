# MXEEditor
A program for unpacking and re-packing MXE files from Valkyria Chronicles to and from CSV files. You are highly recommended to read the entirety of the [User Information](#user-information) section of this readme, since it contains the information on how to run the program and how to edit the output CSV files.

## User Information
### Known Issues
- You must currently run MXEEditor from the folder it is located in. If the current working directory is different, it will fail to locate its configuration files.
- Unpacking an MXE and then re-packing it does not guarantee that the files will be byte-for-byte identical. This is for two reasons:
    - Strings. The MXEs contain both SHIFT-JIS and UTF-8 strings, but the game appears to only be able to decode strings as SHIFT-JIS. pyValkLib therefore writes strings are marked as "UTF-8" as "SHIFT-JIS" where it can. This will tend to increase the size of MXEs.
    - File Metadata. The MXE files contain compressed metadata in the form of POF0, ENRS, and CCRS data chunks. Whilst the POF0 can be exactly recompressed, the ENRS and CCRS use a more complicated compression mechanism. The version of the compression used by the game is actually very inefficient; pyValkLib compresses this data more efficiently (but in a logically equivalent way). Compressing the data to byte-for-byte reproduce the "inefficient" version can be done but it requires work. Since pyValkLib compressed the data more efficiently, this tends to decrease the size of MXEs (`game_info_game_param.mxe` shrinks by >50%!).
    All other data should be byte-for-byte identical, other than string pointers due to the aforementioned string re-encoding.
    
### Usage
MXEEditor can be used to pack or unpack MXE files for Valkyria Chronicles from the command line. In the commands below, `[MXEEditor]` is to be replaced by:
- `python MXEEditor.py` if you are running the Python source directly,
- `path\to\MXEEditor.exe` if you are running a Windows release,
- The path to a compiled executable you have generated yourself for your Operating System in some fashion.

```
- Unpack a single file: [MXEEditor] -u path/to/file.mxe [-o path/to/output/dir]
- Unpack many files   : [MXEEditor] -r -u path/to/dir/of/mxes [-o path/to/output/dir]
- Pack a single file  : [MXEEditor] -p path/to/dir [-o path/to/output/dir]
- Pack many files     : [MXEEditor] -r -p path/to/dir/of/unpacked/mxes [-o path/to/output/dir]
```

In the above commands, if the output directory is not specified, the output of the program will be placed into the same directory as the input data.

### Editing MXE CSV files
Upon unpacking an MXE, you will find up to three folders, plus an `assets.csv` file:
- `entities`
- `params`
- `paths`

MXE files mostly contain chunks of data collected in groups the MXEEditor calls `Parameter Sets`. However, most Parameter Sets are grouped into `Entities` by the game, where each `Entity` represents a Game Object and a `Parameter Set` describes some aspect of that `Entity`. Therefore, we'll start the explanation by looking at the `entities` folder.

**NOTE: ALL CSV FILES ARE UTF-8 ENCODED. YOU SHOULD OPEN, EDIT, AND SAVE THESE CSV FILES USING UTF-8 ENCODING ONLY.**

#### Entities

Inside the `entities` folder, you will find a series of `csv` files. Each `csv` file contains data on a particular type of `Entity`. If you open up a csv --- below we use the example of `EnMovePath.csv` from `vmap_set_001_00` --- you will see something similar to the following:

| ID | Name | Controller Entity | Unknown | EnMovePathParam |
| -- | ---- | ----------------- | ------- | --------------- |
|2952|?????????????????????_5|0| |57|

- ID is the ID number of the Entity. It must be unique.
- Name is the internal name of Entity. It probably can be whatever you want.
- The purpose of Controller Entity is unclear; if it is `0` then there is no Controller, but if there is a Controller then the ID of that Entity is given here.
- The purpose of the Unknown column is unclear. It appears to be a 64-bit integer attached to some Entities, and may be some kind of hash value. Leave this cell blank if you do not wish to enter data here - most Entities will not have anything in this column.
- After these four, there are the `Parameter Sets` attached to the `Entity`. For the example above, there is only one `Parameter Set` attached. The name of the column gives the type of the `Parameter Set` - in this case, `EnMovePathParam`. The given row tells us that the `Parameter Set` with ID `57` in the `params/EnMovePathParam.csv` file is attached to this `Entity`.

This is the basic operation of Entities, and since `Entities` represent Game Objects, the `entities` folder should be your first port of call if you are looking to add Game Objects to an MXE. Let's move on to `Parameter Sets`.

#### Parameter Sets

Inside the `params` folder, you will find more `csv` files corresponding to each type of `Parameter Set` inside the MXE. Since the `Entity` we were looking at linked to an `EnMovePathParam`, let's have a look at the `EnMovePathParam.csv` from `vmap_set_001_00`:

| ID | Name | unknown_0x00 | unknown_0x04 | ... | path_id | unknown_0x0114 | unknown_0x0118 |
| -- | ---- | ------------ | ------------ | --- | ------- | -------------- | -------------- |
| 57 | ?????????????????????_5 | 1 | 0 | ... | 1 | 1002 | 0 |

Above, the leftmost and rightmost columns of the CSV file is reproduced. The columns:

- ID is the ID number of the Parameter Set. It must be unique. **Also, all IDs are currently global across all Parameter Sets in the MXE. The IDs must also form a contiguous series. Packing will fail, and you will be told the reason for the error, if your IDs violate these constraints. They will hopefully be relaxed in the future.**
- Name is the name of the Parameter Set. IT probably can be set to anything.
- The remaining columns are the data contained inside the `Parameter Set`. Most of it is currently unknown (you can help by identifying data and creating an [issue](https://github.com/Pherakki/MXEEditor/issues)!).

There are two special kinds of data contained in the Parameter Sets that we should pay additional attention to: `paths` and `assets`. These both link to the remaining two pieces of data unpacked by the file. You should be able to tell if a data type is a `path` or `asset` ID, because these have all been identified and the columns are appropriately named to tell you it is a `path` or `asset`. The `EnMovePathParam` Parameter Set contains a path in `path_id`, so let's move on to the `paths` now.

#### Paths

The path data is contained within the `paths` section of the unpacked MXE. This is a collection of [Directed Graphs](https://en.wikipedia.org/wiki/Directed_graph) that represent many things, such as searchlight paths or AI pathfinding helpers.

Inside the `paths` folder you will see another set of folders (probably with Japanese names), and a `paths.csv`. Inside `paths.csv`, you'll find something like this:

| ID | Name |
| -- | ---- |
| 0 | ??????????????????????????? |
| 1 | ?????????????????????_4 |
| 2 | ?????????????????????????????????|
| ... | ... |

This is very simple: it gives a list of names for each graph, and attaches an ID to each name. **Again, these IDs must be unique and form a contiguous list.** Each of these names should correspond to one of the `paths` sub-folders. In the Parameter Set we were just looking at for `EnMovePathParam`, it references the path `1`. We can see in `paths.csv` that this corresponds to the graph `?????????????????????_4`. We can therefore find the data for this folder in `paths/?????????????????????_4`. Inside this folder, we'll find some CSV files. Some graphs, such as the one in this example, are actually empty and contain no CSV files. We can go to another graph, such as `?????????????????????????????????`, to see one that contains CSV files. Each CSV file is given a number, *e.g.* `0.csv`. **These numbers must, again, be unique and sequential.** These represent **disconnected components** of the graph. These is only one graph with more than one disconnected component (which we will call a `subgraph`) in the entire game; most graphs have a single `subgraph`. Let's open up `0.csv`.

| ID | Node Parameter | Next Node 1 | Node Node 1 Parameters |
| -- | -------------- | ----------- | ---------------------- |
| 0 | 5 | 1 | 43 |
| 1 | 6 | 2 | 44 |
| ... | ... | ... | ... |

Each row corresponds to a `Node` in the Graph. **The IDs must be unique and contiguous**. Each `Node` has an attached `Parameter`; the type is dictated by the type of Graph. Since this Graph is attached to an `SlgEnAreaSurveillanceParam`, the `Node Parameter`s for this Graph must be `SlgEnAreaSurveillancePathNodeParam` - you can check the type in the configuration files for the parameters, given in `pyValkLib/configuration/MXE/parameters`.

After these two columns, you can have an arbitrary number of columns representing nodes that are connected to the Node for that row. For example, we can see in the table above that Node 0 is forwards-connected to Node 1, and Node 1 is forwards-connected to Node 2 (*i.e.* in the graph, an arrow would come from Node 0 and point towards Node 1, and from Node 1 to Node 2). Each Connection must also have an attached `Parameter Set`, and this is always `void` type.

#### Assets
Finally, we come to `assets`. Some `Parameter Sets` reference `assets` by ID. If we look inside `assets.csv`, we can see what `Assets` are referenced in the MXE.

| ID | Unknown ID 1 | Unknown ID 2 | Asset Path |
| -- | ------------ | ------------ | ---------- |
| 0 | -1 | -1 | ../resource/mx/valcA02aD.htx |
| 1 | -1 | -1 | ../resource/mx/valcE01aB.htx |
| 2 | -1 | -1 | ../resource/mx/valcE51aB.htx |

- ID is the ID of the Asset. Once again: all IDs must be unique and contiguous.
- Unknown ID 1 is an unknown ID. It is only larger than -1 for some HTX (texture) files. It is speculated to be related to the `MxParameterTextureMerge` Parameter Set.
- Unknown ID 2 is an unknown ID. It is only larger than -1 for some files that are not HTX (texture) files. It is speculated to be related to the `MxParameterMergeFile` Parameter Set.
- `Asset Path` is the on-disk location of the asset. Note that each `asset slot` in a `Parameter Set` can only be linked to a specific Asset Type; if this is the wrong type then MXEEditor will throw an error on repacking. The asset type should be clear from the column name in the Parameter Set csv file; it can also be checked in the Parameter definitions files at `pyValkLib/configuration/MXE/parameters`. Some parameters are listed as "unknown asset"s in the Parameter Set CSVs - these are never attached to any Assets in the vanilla files and therefore have unknown types. MXEEditor will therefore allow any asset to be assigned to these slots - just bear in mind that if you do this you might crash the game!

## Developer Information
### Requirements
If you wish to run the source code, Python 3.6+ is required.
MXEEditor relies on [pyValkLib](https://github.com/Pherakki/pyValkLib), but it includes a copy of the version it is built against in the repository. You should therefore require no other dependencies.

### Compilation
MXEEditor is currently written in Python, so if you have Python 3.6+ installed you should be able to run the source code directly. However, today there are multiple options to compile, freeze, or otherwise package Python into an executable file. Windows releases are generated with [Nuitka](https://github.com/Nuitka/Nuitka), which should work for many other Operating Systems also. Nuitka can be installed to your system Python distribution with `pip install nuitka`, or to your Conda environment following instructions on the [Anaconda documentation for Nuitka](https://anaconda.org/conda-forge/nuitka).

Once you have Nuitka installed, the following steps are followed to create an executable:
1. From the MXEEditor root directory, run `python -m nuitka MXEEditor.py --show-progress --follow-imports --onefile`
2. If you copy the generated executable elsewhere, also copy the `configuration` folder of `pyValkLib`, such that the folder `pyValkLib/configuration/...` is in the same directory as `MXEEditor.exe`.

### Future Plans
- Find a way to calculate the two unknown IDs in the Assets table (speculated to be related to the TextureMerge and MergeFile entries in an MXE). If these are calculable, then the assets table can be eliminated, removing a potential source of user error.
- Understand if some MXEs reference IDs present in other MXEs; if they don't, then the "global" IDs of parameters can be replaced with IDs "local" to each CSV file. This will cut out the annoyance of needing to have a perfect series of ID numbers for the parameters.
- Come up with some way that allows the user to not need to have a contiguous series of IDs for parameter sets, paths, and assets; the MXEEditor should be able to map these to a contiguous range if necessary or feed them directly to pyValkLib if not.
- Add an "auto" option to Path Edges which auto-generates a new `void` parameter for them.
- Maybe add a GUI for editing the MXE data that is more difficult to make structural mistakes with than CSV files.

### Features for v1.0
- All Parameter Set values given names
- Implement any of the "future plans" items that are practical and useful
- Support for Valkyria Chronicles 4
