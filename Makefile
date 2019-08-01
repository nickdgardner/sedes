WORKS = \
	homerichymns \
 	iliad \
 	odyssey \
 	shield \
 	theogony \
 	worksanddays \

WORKS_CSV = $(addprefix corpus/,$(addsuffix .csv,$(WORKS)))

all.csv: $(WORKS_CSV)
	(head -q -n 1 "$<"; tail -q -n +2 $^) > "$@"

corpus/homerichymns.csv: WORK_IDENTIFIER = Hymns
corpus/iliad.csv:        WORK_IDENTIFIER = Il.
corpus/odyssey.csv:      WORK_IDENTIFIER = Od.
corpus/shield.csv:       WORK_IDENTIFIER = Shield
corpus/theogony.csv:     WORK_IDENTIFIER = Theog.
corpus/worksanddays.csv: WORK_IDENTIFIER = WD
%.csv: %.xml
	src/tei2csv "$(WORK_IDENTIFIER)" "$<" > "$@"
.INTERMEDIATE: $(WORKS_CSV)

.DELETE_ON_ERROR:
