> {-# LANGUAGE UnicodeSyntax #-}

> module Smallestnumber 
> where

find the smallest free number in the range [1 .. 100]
	
	minfree :: [Nat] → Nat
	minfree xs = head ([0 .. ] \\ xs)

The function minfree is executable but requires Θ(n2) steps 
on a list of length n in the worst case.

> minfree ∷ [Integer] → Integer
> minfree xs = head([1..100] \\ xs)

The expression us \\ vs denotes the list of those elements of us that remain
after removing any elements in vs:

	(\\) ∷ Eqa ⇒ [a] → [a] → [a] 
	us \\ vs = filter(notElem vs)us

Filtering the lists at the worst case, it requires n steps

> (\\) ∷ [Integer] → [Integer] → [Integer]
> us \\ vs = filter (notElem' vs) us

Evaluating i notElem [n−1, n−2 .. 1] at the worst case,
it require n steps

> notElem' ∷ [Integer] → Integer → Bool
> notElem' a n = notElem n (rmElem a [1..100])

This part is not accounted on the performance time calculation

> rmElem ∷ [Integer] → [Integer] → [Integer]
> rmElem _ []           = []
> rmElem [] ys          = ys
> rmElem xs (y:ys) 
> 	    | elem y xs     = rmElem xs ys
>       | notElem y xs  = y : (rmElem xs ys)