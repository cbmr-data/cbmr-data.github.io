#!/usr/bin/env Rscript
library(argparser)

parser <- arg_parser("This is my script!")

parser <- add_argument(parser, "input_file", help="My data")
parser <- add_argument(parser, "--p-value", default=0.05, help="Maximum P-value")

args <- parse_args(parser)
cat("I would process the file", args$input_file, "with a max P-value of", args$p_value, "\n")
