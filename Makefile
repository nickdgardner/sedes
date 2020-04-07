WORKS = \
	aratus \
	argonautica \
	callimachushymns \
	homerichymns \
 	iliad \
	nonnusdionysiaca \
 	odyssey \
	quintussmyrnaeus \
 	shield \
	theocritus \
 	theogony \
 	worksanddays \

WORK_IDENTIFIER_aratus           = Phaen.
WORK_IDENTIFIER_argonautica      = Argon.
WORK_IDENTIFIER_callimachushymns = Callim.Hymn
WORK_IDENTIFIER_homerichymns     = Hom.Hymn
WORK_IDENTIFIER_iliad            = Il.
WORK_IDENTIFIER_nonnusdionysiaca = Dion.
WORK_IDENTIFIER_odyssey          = Od.
WORK_IDENTIFIER_quintussmyrnaeus = Q.S.
WORK_IDENTIFIER_shield           = Sh.
WORK_IDENTIFIER_theocritus       = Theoc.
WORK_IDENTIFIER_theogony         = Theog.
WORK_IDENTIFIER_worksanddays     = W.D.

WORKS_CSV = $(addprefix corpus/,$(addsuffix .csv,$(WORKS)))

all.csv: $(WORKS_CSV)
	(sed -n -e '1p' "$<"; for x in $^; do sed -e '1d' $$x; done) > "$@"

corpus/%.csv: corpus/%.xml
	src/tei2csv "$(WORK_IDENTIFIER_$*)" "$<" > "$@"
.INTERMEDIATE: $(WORKS_CSV)

PYTHON = python3

.PHONY: test
test:
	(cd src && "$(PYTHON)" -m unittest)

.PHONY: fonts
fonts: \
	web-demo/fonts/SIL\ Open\ Font\ License.txt \
	web-demo/fonts/Cardo-Regular.woff \
	web-demo/fonts/Cardo-Italic.woff \
	web-demo/fonts/Cardo-Bold.woff

web-demo/fonts/SIL\ Open\ Font\ License.txt: fonts/cardo.zip
	unzip -D -o "$<" "$(notdir $@)"
	mv -f "$(notdir $@)" "$@"

%.ttf: fonts/cardo.zip
	unzip -D -o "$<" "$(notdir $@)"

web-demo/fonts/%.woff: %.ttf
	mkdir -p web-demo/fonts
	fontforge -lang ff -script fonts/subset-greek.ff "$<" "$@"

.DELETE_ON_ERROR:
