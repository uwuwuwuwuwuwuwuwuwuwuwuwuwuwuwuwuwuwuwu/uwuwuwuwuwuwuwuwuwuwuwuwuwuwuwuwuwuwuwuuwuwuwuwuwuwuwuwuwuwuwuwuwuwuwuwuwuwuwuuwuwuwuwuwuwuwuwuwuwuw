module Main where

import Data.List (cycle)

-- uwu string of infinite length
uwu :: String
uwu = cycle "uw"

main :: IO ()
main = putStr uwu -- maximum laze
