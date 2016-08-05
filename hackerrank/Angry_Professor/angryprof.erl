%%% Author: Liang Lin
%%% Email: lianglin@outlook.com
%%% Date: 2016-04-07
-module(angryprof).
-export([main/0]).

main() ->

    { ok, [T]} = io:fread("", "~d"),
    T_list = lists:seq(1,T),
    lists:foreach( fun(T0) ->
            { ok, [N,K]} = io:fread("", "~d~d"),
            A = read_array(N,"~d"),
            OnTime = ontime(A, 0),
            if OnTime >= K -> io:fwrite("~s~n", ["NO"]);
               true -> io:fwrite("~s~n", ["YES"])
            end
    end,T_list),
    
    true.

read_array(0,D) -> [];
read_array(N,D) -> 
   {ok, [X]} = io:fread("", D),
   [X | read_array(N-1,D)].

read_2darray(0,M,D) -> [];
read_2darray(N,M,D) ->
   Q=read_array(M,D),
   [Q | read_2darray(N-1,M,D)].
   

ontime([H|T], Count) when H =< 0 -> 
    ontime(T, Count+1);
ontime([_|T], Count) ->
    ontime(T, Count);
ontime([], Count) ->
    Count.

