# View modes
VIEW_REMOTE_BIT = 0x1
VIEW_IN_PERSON_BIT = 0x2
VIEW_HYBRID_BIT = 0x4

# URL to get data from
SCHED_OF_CLASSES_URL = "https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm"

# Required query parameters
BROWSER_SETTINGS = "&xsoc_term=&loggedIn=false&tabNum=" 
QUERY_PARAMS = "&_selectedSubjects=1"\
"&schedOption1=true&_schedOption1=on&_schedOption11=on&_schedOption12=on&schedOption2=true"\
"&_schedOption2=on&_schedOption4=on&_schedOption5=on&_schedOption3=on&_schedOption7=on"\
"&_schedOption8=on&_schedOption13=on&_schedOption10=on&_schedOption9=on&schDay=M&_schDay=on"\
"&schDay=T&_schDay=on&schDay=W&_schDay=on&schDay=R&_schDay=on&schDay=F&_schDay=on&schDay=S"\
"&_schDay=on&schStartTime=12%3A00&schStartAmPm=0&schEndTime=12%3A00&schEndAmPm=0"\
"&_selectedDepartments=1&schedOption1Dept=true&_schedOption1Dept=on&_schedOption11Dept=on"\
"&_schedOption12Dept=on&schedOption2Dept=true&_schedOption2Dept=on&_schedOption4Dept=on"\
"&_schedOption5Dept=on&_schedOption3Dept=on&_schedOption7Dept=on&_schedOption8Dept=on"\
"&_schedOption13Dept=on&_schedOption10Dept=on&_schedOption9Dept=on&schDayDept=M&_schDayDept=on"\
"&schDayDept=T&_schDayDept=on&schDayDept=W&_schDayDept=on&schDayDept=R&_schDayDept=on"\
"&schDayDept=F&_schDayDept=on&schDayDept=S&_schDayDept=on&schStartTimeDept=12%3A00"\
"&schStartAmPmDept=0&schEndTimeDept=12%3A00&schEndAmPmDept=0&courses=&sections="\
"&instructorType=begin&instructor=&titleType=contain&title=&_hideFullSec=on"\
"&showPopup=true&_showPopup=on"

# Default query parameters
DEFAULT_TERM = "selectedTerm=FA20"
DEFAULT_SUBJS = "&selectedSubjects=AIP+&selectedSubjects=AAS+"\
"&selectedSubjects=AWP+&selectedSubjects=ANES&selectedSubjects=ANBI&selectedSubjects=ANAR"\
"&selectedSubjects=ANTH&selectedSubjects=ANSC&selectedSubjects=AESE&selectedSubjects=BENG"\
"&selectedSubjects=BNFO&selectedSubjects=BIEB&selectedSubjects=BICD&selectedSubjects=BIPN"\
"&selectedSubjects=BIBC&selectedSubjects=BGGN&selectedSubjects=BGRD&selectedSubjects=BGSE"\
"&selectedSubjects=BILD&selectedSubjects=BIMM&selectedSubjects=BISP&selectedSubjects=BIOM"\
"&selectedSubjects=CENG&selectedSubjects=CHEM&selectedSubjects=CHIN&selectedSubjects=CCS+"\
"&selectedSubjects=CLIN&selectedSubjects=CLRE&selectedSubjects=COGS&selectedSubjects=COMM"\
"&selectedSubjects=COGR&selectedSubjects=CSS+&selectedSubjects=CSE+&selectedSubjects=CGS+"\
"&selectedSubjects=CAT+&selectedSubjects=TDDM&selectedSubjects=TDHD&selectedSubjects=TDMV"\
"&selectedSubjects=TDTR&selectedSubjects=DSC+&selectedSubjects=DSE+&selectedSubjects=DERM"\
"&selectedSubjects=DSGN&selectedSubjects=DOC+&selectedSubjects=DDPM&selectedSubjects=ECON"\
"&selectedSubjects=EDS+&selectedSubjects=ERC+&selectedSubjects=ECE+&selectedSubjects=EMED"\
"&selectedSubjects=ENG+&selectedSubjects=ENVR&selectedSubjects=ESYS&selectedSubjects=ETIM"\
"&selectedSubjects=ETHN&selectedSubjects=EXPR&selectedSubjects=FMPH&selectedSubjects=FPM+"\
"&selectedSubjects=FILM&selectedSubjects=GPCO&selectedSubjects=GPEC&selectedSubjects=GPGN"\
"&selectedSubjects=GPIM&selectedSubjects=GPLA&selectedSubjects=GPPA&selectedSubjects=GPPS"\
"&selectedSubjects=GLBH&selectedSubjects=HITO&selectedSubjects=HIAF&selectedSubjects=HIEA"\
"&selectedSubjects=HIEU&selectedSubjects=HILA&selectedSubjects=HISC&selectedSubjects=HINE"\
"&selectedSubjects=HIUS&selectedSubjects=HIGR&selectedSubjects=HILD&selectedSubjects=HDS+"\
"&selectedSubjects=HUM+&selectedSubjects=INTL&selectedSubjects=JAPN&selectedSubjects=JWSP"\
"&selectedSubjects=LATI&selectedSubjects=LHCO&selectedSubjects=LISL&selectedSubjects=LIAB"\
"&selectedSubjects=LIDS&selectedSubjects=LIFR&selectedSubjects=LIGN&selectedSubjects=LIGM"\
"&selectedSubjects=LIHL&selectedSubjects=LIIT&selectedSubjects=LIPO&selectedSubjects=LISP"\
"&selectedSubjects=LTAM&selectedSubjects=LTCH&selectedSubjects=LTCO&selectedSubjects=LTCS"\
"&selectedSubjects=LTEU&selectedSubjects=LTFR&selectedSubjects=LTGM&selectedSubjects=LTGK"\
"&selectedSubjects=LTIT&selectedSubjects=LTKO&selectedSubjects=LTLA&selectedSubjects=LTRU"\
"&selectedSubjects=LTSP&selectedSubjects=LTTH&selectedSubjects=LTWR&selectedSubjects=LTEN"\
"&selectedSubjects=LTWL&selectedSubjects=LTEA&selectedSubjects=MMW+&selectedSubjects=MBC+"\
"&selectedSubjects=MATS&selectedSubjects=MATH&selectedSubjects=MSED&selectedSubjects=MAE+"\
"&selectedSubjects=MED+&selectedSubjects=MCWP&selectedSubjects=MUS+&selectedSubjects=NANO"\
"&selectedSubjects=NEU+&selectedSubjects=NEUG&selectedSubjects=OPTH&selectedSubjects=ORTH"\
"&selectedSubjects=PATH&selectedSubjects=PEDS&selectedSubjects=PHAR&selectedSubjects=SPPS"\
"&selectedSubjects=PHIL&selectedSubjects=PHYS&selectedSubjects=POLI&selectedSubjects=PSY+"\
"&selectedSubjects=PSYC&selectedSubjects=RMAS&selectedSubjects=RAD+&selectedSubjects=MGT+"\
"&selectedSubjects=RELI&selectedSubjects=RMED&selectedSubjects=REV+&selectedSubjects=SOMI"\
"&selectedSubjects=SOMC&selectedSubjects=SIOC&selectedSubjects=SIOG&selectedSubjects=SIOB"\
"&selectedSubjects=SIO+&selectedSubjects=SXTH&selectedSubjects=SOCG&selectedSubjects=SOCE"\
"&selectedSubjects=SOCI&selectedSubjects=SE++&selectedSubjects=SURG&selectedSubjects=TDAC"\
"&selectedSubjects=TDDE&selectedSubjects=TDDR&selectedSubjects=TDGE&selectedSubjects=TDGR"\
"&selectedSubjects=TDHT&selectedSubjects=TDPW&selectedSubjects=TDPR&selectedSubjects=TWS+"\
"&selectedSubjects=TMC+&selectedSubjects=USP+&selectedSubjects=UROL&selectedSubjects=VIS+"\
"&selectedSubjects=WARR&selectedSubjects=WCWP&selectedSubjects=WES+"

# Default, which queries everything
DEFAULT_QUERY_PARAMS = DEFAULT_TERM + BROWSER_SETTINGS + DEFAULT_SUBJS + QUERY_PARAMS
