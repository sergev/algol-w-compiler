(* location.ml 

--

This file is part of Awe. Copyright 2012 Glyn Webster.

Awe is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Awe is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public
License along with Awe.  If not, see <http://www.gnu.org/licenses/>.

*)

type t = int * int * int

let filenames : string DynArray.t = DynArray.create "" ;;
let filenumbers : (string, int) Hashtbl.t = Hashtbl.create 20 ;;

let name_of_number number = 
  DynArray.get filenames number

let number_of_name name = 
    try Hashtbl.find filenumbers name
    with Not_found -> DynArray.length filenames - 1

let set_filename new_filename = 
  DynArray.add filenames new_filename ;
  Hashtbl.add filenumbers new_filename (DynArray.length filenames - 1)

let create filename line char = 
  let number = 
    try
      Hashtbl.find filenumbers filename
    with Not_found ->
      DynArray.add filenames filename ;
      let n = DynArray.length filenames - 1 in
      Hashtbl.add filenumbers filename n ;
      n
  in
  (number, line, char)

let of_position position = 
  let file = 
    if position.Lexing.pos_fname <> "" then position.Lexing.pos_fname
    else name_of_number (DynArray.length filenames - 1)  (* last set_filename name *)
  in
  let line = position.Lexing.pos_lnum in
  let char = position.Lexing.pos_cnum - position.Lexing.pos_bol in
  create file line char

let filename (n, _, _) = name_of_number n
let file_number (n, _, _) = n
let line (_, n, _) = n
let column (_, _, n) = n
    
let to_string loc = 
  Printf.sprintf "%s:%i:%i:" (filename loc) (line loc) (column loc + 1)

(* end *)
