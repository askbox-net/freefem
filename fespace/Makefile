FREEFEM = FreeFem++
FLAG = -nw # no window
CONVERT = convert
PANDOC = pandoc
PANDOC_FLAGS = --pdf-engine=lualatex -V documentclass=bxjsarticle -V classoption=pandoc --filter pandoc-include 

SRC_DIR = .
OBJ_DIR = ./outputs

SRC = $(wildcard $(SRC_DIR)/*edp)
SRC_MD = $(wildcard $(SRC_DIR)/*.md)
SRC_EPS = $(wildcard $(OBJ_DIR)/*.eps)

OBJ_EPS = $(addprefix $(OBJ_DIR)/, $(SRC:%.edp=%.eps))
OBJ_PNG = $(SRC_EPS:%.eps=%.png)
OBJ_PDF = $(addprefix $(OBJ_DIR)/, $(SRC_MD:%.md=%.pdf))
#OBJECTS  = $(addprefix $(OBJDIR)/, $(SOURCES:.cpp=.o))

all: $(OBJ_DIR) $(OBJ_EPS)

$(OBJ_DIR):
	mkdir -p $@

$(OBJ_DIR)/%.eps: %.edp
	$(FREEFEM) $(FLAG) $^

png: $(OBJ_EPS) $(OBJ_PNG)

%.png: %.eps
	$(CONVERT) $^ $@

pdf: $(OBJ_PNG) $(OBJ_PDF)

$(OBJ_DIR)/%.pdf: %.md
	$(PANDOC) $^ $(PANDOC_FLAGS) -o $@

clean:
	rm -rf $(OBJ_DIR)

