FREEFEM = FreeFem++
FLAG = -nw # no window
CONVERT = convert
PANDOC = pandoc

SRCDIR = .
OUTPUT = ./outputs

SRC = $(wildcard $(SRCDIR)/*edp)
SRC_MD = $(wildcard $(SRCDIR)/*.md)
SRC_EPS = $(wildcard $(OUTPUT)/*.eps)

OBJ_EPS = $(addprefix $(OUTPUT)/, $(SRC:%.edp=%.eps))
OBJ_PNG = $(SRC_EPS:%.eps=%.png)
OBJ_PDF = $(addprefix $(OUTPUT)/, $(SRC_MD:%.md=%.pdf))
#OBJECTS  = $(addprefix $(OBJDIR)/, $(SOURCES:.cpp=.o))

all: $(OUTPUT) $(OBJ_EPS)

$(OUTPUT):
	mkdir -p $@

$(OUTPUT)/%.eps: %.edp
	$(FREEFEM) $(FLAG) $^

png: $(OBJ_EPS) $(OBJ_PNG)

%.png: %.eps
	$(CONVERT) $^ $@

pdf: $(OBJ_PNG) $(OBJ_PDF)

$(OUTPUT)/%.pdf: %.md
	$(PANDOC) $^ --filter pandoc-include -o $@

clean:
	rm -rf $(OUTPUT)/*.*

