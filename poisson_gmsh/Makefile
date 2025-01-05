FREEFEM = freefem++
FLAGS = -nw # no window
GMSH = gmsh
GNUPLOT = gnuplot
PANDOC = pandoc
PANDOC_FLAGS = --pdf-engine=lualatex -V documentclass=bxjsarticle -V classoption=pandoc --filter pandoc-include 
PYTHON = python3

SRC_DIR = .
OBJ_DIR = ./outputs

SRC = $(wildcard $(SRC_DIR)/*.edp)
SRC_MD = $(wildcard $(SRC_DIR)/*.md)

OBJ_EPS = $(addprefix $(OBJ_DIR)/, $(SRC:%.edp=%.eps))
OBJ_PDF = $(addprefix $(OBJ_DIR)/, $(SRC_MD:%.md=%.pdf))

all: $(OBJ_DIR) $(OBJ_EPS)

$(OBJ_DIR):
	mkdir -p $@

$(OBJ_DIR)/%.eps: %.edp
	gmsh -2 poisson.geo -format msh2 -o ./outputs/poisson.msh
	$(FREEFEM) $(FLAG) $^

pdf: $(OBJ_EPS) $(OBJ_PDF)

$(OBJ_DIR)/%.pdf: %.md
	$(PYTHON) plot_trisuf.py
	$(GNUPLOT) ./gnuplot_poisson.gp
	$(PANDOC) $^ $(PANDOC_FLAGS) -o $@

clean:
	rm -rf $(OBJ_DIR) *.eps *.txt

