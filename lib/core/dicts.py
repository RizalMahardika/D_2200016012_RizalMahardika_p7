#!/usr/bin/env python

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import CONTENT_TYPE
from lib.core.enums import DBMS
from lib.core.enums import OS
from lib.core.enums import POST_HINT
from lib.core.settings import ACCESS_ALIASES
from lib.core.settings import ALTIBASE_ALIASES
from lib.core.settings import BLANK
from lib.core.settings import CACHE_ALIASES
from lib.core.settings import CRATEDB_ALIASES
from lib.core.settings import CUBRID_ALIASES
from lib.core.settings import DB2_ALIASES
from lib.core.settings import DERBY_ALIASES
from lib.core.settings import EXTREMEDB_ALIASES
from lib.core.settings import FIREBIRD_ALIASES
from lib.core.settings import FRONTBASE_ALIASES
from lib.core.settings import H2_ALIASES
from lib.core.settings import HSQLDB_ALIASES
from lib.core.settings import INFORMIX_ALIASES
from lib.core.settings import MAXDB_ALIASES
from lib.core.settings import MCKOI_ALIASES
from lib.core.settings import MIMERSQL_ALIASES
from lib.core.settings import MONETDB_ALIASES
from lib.core.settings import MSSQL_ALIASES
from lib.core.settings import MYSQL_ALIASES
from lib.core.settings import NULL
from lib.core.settings import ORACLE_ALIASES
from lib.core.settings import PGSQL_ALIASES
from lib.core.settings import PRESTO_ALIASES
from lib.core.settings import RAIMA_ALIASES
from lib.core.settings import SQLITE_ALIASES
from lib.core.settings import SYBASE_ALIASES
from lib.core.settings import VERTICA_ALIASES
from lib.core.settings import VIRTUOSO_ALIASES
from lib.core.settings import CLICKHOUSE_ALIASES

FIREBIRD_TYPES = {
    261: "BLOB",
    14: "CHAR",
    40: "CSTRING",
    11: "D_FLOAT",
    27: "DOUBLE",
    10: "FLOAT",
    16: "INT64",
    8: "INTEGER",
    9: "QUAD",
    7: "SMALLINT",
    12: "DATE",
    13: "TIME",
    35: "TIMESTAMP",
    37: "VARCHAR",
}

INFORMIX_TYPES = {
    0: "CHAR",
    1: "SMALLINT",
    2: "INTEGER",
    3: "FLOAT",
    4: "SMALLFLOAT",
    5: "DECIMAL",
    6: "SERIAL",
    7: "DATE",
    8: "MONEY",
    9: "NULL",
    10: "DATETIME",
    11: "BYTE",
    12: "TEXT",
    13: "VARCHAR",
    14: "INTERVAL",
    15: "NCHAR",
    16: "NVARCHAR",
    17: "INT8",
    18: "SERIAL8",
    19: "SET",
    20: "MULTISET",
    21: "LIST",
    22: "ROW (unnamed)",
    23: "COLLECTION",
    40: "Variable-length opaque type",
    41: "Fixed-length opaque type",
    43: "LVARCHAR",
    45: "BOOLEAN",
    52: "BIGINT",
    53: "BIGSERIAL",
    2061: "IDSSECURITYLABEL",
    4118: "ROW (named)",
}

SYBASE_TYPES = {
    14: "floatn",
    8: "float",
    15: "datetimn",
    12: "datetime",
    23: "real",
    28: "numericn",
    10: "numeric",
    27: "decimaln",
    26: "decimal",
    17: "moneyn",
    11: "money",
    21: "smallmoney",
    22: "smalldatetime",
    13: "intn",
    7: "int",
    6: "smallint",
    5: "tinyint",
    16: "bit",
    2: "varchar",
    18: "sysname",
    25: "nvarchar",
    1: "char",
    24: "nchar",
    4: "varbinary",
    80: "timestamp",
    3: "binary",
    19: "text",
    20: "image",
}

ALTIBASE_TYPES = {
    1: "CHAR",
    12: "VARCHAR",
    -8: "NCHAR",
    -9: "NVARCHAR",
    2: "NUMERIC",
    6: "FLOAT",
    8: "DOUBLE",
    7: "REAL",
    -5: "BIGINT",
    4: "INTEGER",
    5: "SMALLINT",
    9: "DATE",
    30: "BLOB",
    40: "CLOB",
    20001: "BYTE",
    20002: "NIBBLE",
    -7: "BIT",
    -100: "VARBIT",
    10003: "GEOMETRY",
}

MYSQL_PRIVS = {
    1: "select_priv",
    2: "insert_priv",
    3: "update_priv",
    4: "delete_priv",
    5: "create_priv",
    6: "drop_priv",
    7: "reload_priv",
    8: "shutdown_priv",
    9: "process_priv",
    10: "file_priv",
    11: "grant_priv",
    12: "references_priv",
    13: "index_priv",
    14: "alter_priv",
    15: "show_db_priv",
    16: "super_priv",
    17: "create_tmp_table_priv",
    18: "lock_tables_priv",
    19: "execute_priv",
    20: "repl_slave_priv",
    21: "repl_client_priv",
    22: "create_view_priv",
    23: "show_view_priv",
    24: "create_routine_priv",
    25: "alter_routine_priv",
    26: "create_user_priv",
}

PGSQL_PRIVS = {
    1: "createdb",
    2: "super",
    3: "catupd",
}

# Reference(s): http://stackoverflow.com/a/17672504
#               http://docwiki.embarcadero.com/InterBase/XE7/en/RDB$USER_PRIVILEGES

FIREBIRD_PRIVS = {
    "S": "SELECT",
    "I": "INSERT",
    "U": "UPDATE",
    "D": "DELETE",
    "R": "REFERENCE",
    "X": "EXECUTE",
    "A": "ALL",
    "M": "MEMBER",
    "T": "DECRYPT",
    "E": "ENCRYPT",
    "B": "SUBSCRIBE",
}

# Reference(s): https://www.ibm.com/support/knowledgecenter/SSGU8G_12.1.0/com.ibm.sqls.doc/ids_sqs_0147.htm
#               https://www.ibm.com/support/knowledgecenter/SSGU8G_11.70.0/com.ibm.sqlr.doc/ids_sqr_077.htm

INFORMIX_PRIVS = {
    "D": "DBA (all privileges)",
    "R": "RESOURCE (create UDRs, UDTs, permanent tables and indexes)",
    "C": "CONNECT (work with existing tables)",
    "G": "ROLE",
    "U": "DEFAULT (implicit connection)",
}

DB2_PRIVS = {
    1: "CONTROLAUTH",
    2: "ALTERAUTH",
    3: "DELETEAUTH",
    4: "INDEXAUTH",
    5: "INSERTAUTH",
    6: "REFAUTH",
    7: "SELECTAUTH",
    8: "UPDATEAUTH",
}

DUMP_REPLACEMENTS = {" ": NULL, "": BLANK}

DBMS_DICT = {
    DBMS.MSSQL: (MSSQL_ALIASES, "python-pymssql", "https://github.com/pymssql/pymssql", "mssql+pymssql"),
    DBMS.MYSQL: (MYSQL_ALIASES, "python-pymysql", "https://github.com/PyMySQL/PyMySQL", "mysql"),
    DBMS.PGSQL: (PGSQL_ALIASES, "python-psycopg2", "https://github.com/psycopg/psycopg2", "postgresql"),
    DBMS.ORACLE: (ORACLE_ALIASES, "python cx_Oracle", "https://oracle.github.io/python-cx_Oracle/", "oracle"),
    DBMS.SQLITE: (SQLITE_ALIASES, "python-sqlite", "https://docs.python.org/3/library/sqlite3.html", "sqlite"),
    DBMS.ACCESS: (ACCESS_ALIASES, "python-pyodbc", "https://github.com/mkleehammer/pyodbc", "access"),
    DBMS.FIREBIRD: (FIREBIRD_ALIASES, "python-kinterbasdb", "http://kinterbasdb.sourceforge.net/", "firebird"),
    DBMS.MAXDB: (MAXDB_ALIASES, None, None, "maxdb"),
    DBMS.SYBASE: (SYBASE_ALIASES, "python-pymssql", "https://github.com/pymssql/pymssql", "sybase"),
    DBMS.DB2: (DB2_ALIASES, "python ibm-db", "https://github.com/ibmdb/python-ibmdb", "ibm_db_sa"),
    DBMS.HSQLDB: (HSQLDB_ALIASES, "python jaydebeapi & python-jpype", "https://pypi.python.org/pypi/JayDeBeApi/ & https://github.com/jpype-project/jpype", None),
    DBMS.H2: (H2_ALIASES, None, None, None),
    DBMS.INFORMIX: (INFORMIX_ALIASES, "python ibm-db", "https://github.com/ibmdb/python-ibmdb", "ibm_db_sa"),
    DBMS.MONETDB: (MONETDB_ALIASES, "pymonetdb", "https://github.com/gijzelaerr/pymonetdb", "monetdb"),
    DBMS.DERBY: (DERBY_ALIASES, "pydrda", "https://github.com/nakagami/pydrda/", None),
    DBMS.VERTICA: (VERTICA_ALIASES, "vertica-python", "https://github.com/vertica/vertica-python", "vertica+vertica_python"),
    DBMS.MCKOI: (MCKOI_ALIASES, None, None, None),
    DBMS.PRESTO: (PRESTO_ALIASES, "presto-python-client", "https://github.com/prestodb/presto-python-client", None),
    DBMS.ALTIBASE: (ALTIBASE_ALIASES, None, None, None),
    DBMS.MIMERSQL: (MIMERSQL_ALIASES, "mimerpy", "https://github.com/mimersql/MimerPy", None),
    DBMS.CLICKHOUSE: (CLICKHOUSE_ALIASES, "clickhouse_connect", "https://github.com/ClickHouse/clickhouse-connect", None),
    DBMS.CRATEDB: (CRATEDB_ALIASES, "python-psycopg2", "https://github.com/psycopg/psycopg2", "postgresql"),
    DBMS.CUBRID: (CUBRID_ALIASES, "CUBRID-Python", "https://github.com/CUBRID/cubrid-python", None),
    DBMS.CACHE: (CACHE_ALIASES, "python jaydebeapi & python-jpype", "https://pypi.python.org/pypi/JayDeBeApi/ & https://github.com/jpype-project/jpype", None),
    DBMS.EXTREMEDB: (EXTREMEDB_ALIASES, None, None, None),
    DBMS.FRONTBASE: (FRONTBASE_ALIASES, None, None, None),
    DBMS.RAIMA: (RAIMA_ALIASES, None, None, None),
    DBMS.VIRTUOSO: (VIRTUOSO_ALIASES, None, None, None),
}

# Reference: https://blog.jooq.org/tag/sysibm-sysdummy1/
FROM_DUMMY_TABLE = {
    DBMS.ORACLE: " FROM DUAL",
    DBMS.ACCESS: " FROM MSysAccessObjects",
    DBMS.FIREBIRD: " FROM RDB$DATABASE",
    DBMS.MAXDB: " FROM VERSIONS",
    DBMS.DB2: " FROM SYSIBM.SYSDUMMY1",
    DBMS.HSQLDB: " FROM INFORMATION_SCHEMA.SYSTEM_USERS",
    DBMS.INFORMIX: " FROM SYSMASTER:SYSDUAL",
    DBMS.DERBY: " FROM SYSIBM.SYSDUMMY1",
    DBMS.MIMERSQL: " FROM SYSTEM.ONEROW",
    DBMS.FRONTBASE: " FROM INFORMATION_SCHEMA.IO_STATISTICS"
}

HEURISTIC_NULL_EVAL = {
    DBMS.ACCESS: "CVAR(NULL)",
    DBMS.MAXDB: "ALPHA(NULL)",
    DBMS.MSSQL: "DIFFERENCE(NULL,NULL)",
    DBMS.MYSQL: "QUARTER(NULL XOR NULL)",
    DBMS.ORACLE: "INSTR2(NULL,NULL)",
    DBMS.PGSQL: "QUOTE_IDENT(NULL)",
    DBMS.SQLITE: "UNLIKELY(NULL)",
    DBMS.H2: "STRINGTOUTF8(NULL)",
    DBMS.MONETDB: "CODE(NULL)",
    DBMS.DERBY: "NULLIF(USER,SESSION_USER)",
    DBMS.VERTICA: "BITSTRING_TO_BINARY(NULL)",
    DBMS.MCKOI: "TONUMBER(NULL)",
    DBMS.PRESTO: "FROM_HEX(NULL)",
    DBMS.ALTIBASE: "TDESENCRYPT(NULL,NULL)",
    DBMS.MIMERSQL: "ASCII_CHAR(256)",
    DBMS.CRATEDB: "MD5(NULL~NULL)",  # Note: NULL~NULL also being evaluated on H2 and Ignite
    DBMS.CUBRID: "(NULL SETEQ NULL)",
    DBMS.CACHE: "%SQLUPPER NULL",
    DBMS.EXTREMEDB: "NULLIFZERO(hashcode(NULL))",
    DBMS.RAIMA: "IF(ROWNUMBER()>0,CONVERT(NULL,TINYINT),NULL))",
    DBMS.VIRTUOSO: "__MAX_NOTNULL(NULL)",
    DBMS.CLICKHOUSE: "halfMD5(NULL) IS NULL",
}

SQL_STATEMENTS = {
    "SQL SELECT statement": (
        "select ",
        "show ",
        " top ",
        " distinct ",
        " from ",
        " from dual",
        " where ",
        " group by ",
        " order by ",
        " having ",
        " limit ",
        " offset ",
        " union all ",
        " rownum as ",
        "(case ",
    ),

    "SQL data definition": (
        "create ",
        "declare ",
        "drop ",
        "truncate ",
        "alter ",
    ),

    "SQL data manipulation": (
        "bulk ",
        "insert ",
        "update ",
        "delete ",
        "merge ",
        "load ",
    ),

    "SQL data control": (
        "grant ",
        "revoke ",
    ),

    "SQL data execution": (
        "exec ",
        "execute ",
        "values ",
        "call ",
    ),

    "SQL transaction": (
        "start transaction ",
        "begin work ",
        "begin transaction ",
        "commit ",
        "rollback ",
    ),

    "SQL administration": (
        "set ",
    ),
}

POST_HINT_CONTENT_TYPES = {
    POST_HINT.JSON: "application/json",
    POST_HINT.JSON_LIKE: "application/json",
    POST_HINT.MULTIPART: "multipart/form-data",
    POST_HINT.SOAP: "application/soap+xml",
    POST_HINT.XML: "application/xml",
    POST_HINT.ARRAY_LIKE: "application/x-www-form-urlencoded; charset=utf-8",
}

OBSOLETE_OPTIONS = {
    "--replicate": "use '--dump-format=SQLITE' instead",
    "--no-unescape": "use '--no-escape' instead",
    "--binary": "use '--binary-fields' instead",
    "--auth-private": "use '--auth-file' instead",
    "--ignore-401": "use '--ignore-code' instead",
    "--second-order": "use '--second-url' instead",
    "--purge-output": "use '--purge' instead",
    "--sqlmap-shell": "use '--shell' instead",
    "--check-payload": None,
    "--check-waf": None,
    "--pickled-options": "use '--api -c ...' instead",
    "--identify-waf": "functionality being done automatically",
}

DEPRECATED_OPTIONS = {
}

DUMP_DATA_PREPROCESS = {
    DBMS.ORACLE: {"XMLTYPE": "(%s).getStringVal()"},  # Reference: https://www.tibcommunity.com/docs/DOC-3643
    DBMS.MSSQL: {"IMAGE": "CONVERT(VARBINARY(MAX),%s)"},
}

DEFAULT_DOC_ROOTS = {
    OS.WINDOWS: ("C:/xampp/htdocs/", "C:/wamp/www/", "C:/Inetpub/wwwroot/"),
    OS.LINUX: ("/var/www/", "/var/www/html", "/var/www/htdocs", "/usr/local/apache2/htdocs", "/usr/local/www/data", "/var/apache2/htdocs", "/var/www/nginx-default", "/srv/www/htdocs", "/usr/local/var/www")  # Reference: https://wiki.apache.org/httpd/DistrosDefaultLayout
}

PART_RUN_CONTENT_TYPES = {
    "checkDbms": CONTENT_TYPE.TECHNIQUES,
    "getFingerprint": CONTENT_TYPE.DBMS_FINGERPRINT,
    "getBanner": CONTENT_TYPE.BANNER,
    "getCurrentUser": CONTENT_TYPE.CURRENT_USER,
    "getCurrentDb": CONTENT_TYPE.CURRENT_DB,
    "getHostname": CONTENT_TYPE.HOSTNAME,
    "isDba": CONTENT_TYPE.IS_DBA,
    "getUsers": CONTENT_TYPE.USERS,
    "getPasswordHashes": CONTENT_TYPE.PASSWORDS,
    "getPrivileges": CONTENT_TYPE.PRIVILEGES,
    "getRoles": CONTENT_TYPE.ROLES,
    "getDbs": CONTENT_TYPE.DBS,
    "getTables": CONTENT_TYPE.TABLES,
    "getColumns": CONTENT_TYPE.COLUMNS,
    "getSchema": CONTENT_TYPE.SCHEMA,
    "getCount": CONTENT_TYPE.COUNT,
    "dumpTable": CONTENT_TYPE.DUMP_TABLE,
    "search": CONTENT_TYPE.SEARCH,
    "sqlQuery": CONTENT_TYPE.SQL_QUERY,
    "tableExists": CONTENT_TYPE.COMMON_TABLES,
    "columnExists": CONTENT_TYPE.COMMON_COLUMNS,
    "readFile": CONTENT_TYPE.FILE_READ,
    "writeFile": CONTENT_TYPE.FILE_WRITE,
    "osCmd": CONTENT_TYPE.OS_CMD,
    "regRead": CONTENT_TYPE.REG_READ
}

# Reference: http://www.w3.org/TR/1999/REC-html401-19991224/sgml/entities.html

HTML_ENTITIES = {
    "quot": 34,
    "amp": 38,
    "apos": 39,
    "lt": 60,
    "gt": 62,
    "nbsp": 160,
    "iexcl": 161,
    "cent": 162,
    "pound": 163,
    "curren": 164,
    "yen": 165,
    "brvbar": 166,
    "sect": 167,
    "uml": 168,
    "copy": 169,
    "ordf": 170,
    "laquo": 171,
    "not": 172,
    "shy": 173,
    "reg": 174,
    "macr": 175,
    "deg": 176,
    "plusmn": 177,
    "sup2": 178,
    "sup3": 179,
    "acute": 180,
    "micro": 181,
    "para": 182,
    "middot": 183,
    "cedil": 184,
    "sup1": 185,
    "ordm": 186,
    "raquo": 187,
    "frac14": 188,
    "frac12": 189,
    "frac34": 190,
    "iquest": 191,
    "Agrave": 192,
    "Aacute": 193,
    "Acirc": 194,
    "Atilde": 195,
    "Auml": 196,
    "Aring": 197,
    "AElig": 198,
    "Ccedil": 199,
    "Egrave": 200,
    "Eacute": 201,
    "Ecirc": 202,
    "Euml": 203,
    "Igrave": 204,
    "Iacute": 205,
    "Icirc": 206,
    "Iuml": 207,
    "ETH": 208,
    "Ntilde": 209,
    "Ograve": 210,
    "Oacute": 211,
    "Ocirc": 212,
    "Otilde": 213,
    "Ouml": 214,
    "times": 215,
    "Oslash": 216,
    "Ugrave": 217,
    "Uacute": 218,
    "Ucirc": 219,
    "Uuml": 220,
    "Yacute": 221,
    "THORN": 222,
    "szlig": 223,
    "agrave": 224,
    "aacute": 225,
    "acirc": 226,
    "atilde": 227,
    "auml": 228,
    "aring": 229,
    "aelig": 230,
    "ccedil": 231,
    "egrave": 232,
    "eacute": 233,
    "ecirc": 234,
    "euml": 235,
    "igrave": 236,
    "iacute": 237,
    "icirc": 238,
    "iuml": 239,
    "eth": 240,
    "ntilde": 241,
    "ograve": 242,
    "oacute": 243,
    "ocirc": 244,
    "otilde": 245,
    "ouml": 246,
    "divide": 247,
    "oslash": 248,
    "ugrave": 249,
    "uacute": 250,
    "ucirc": 251,
    "uuml": 252,
    "yacute": 253,
    "thorn": 254,
    "yuml": 255,
    "OElig": 338,
    "oelig": 339,
    "Scaron": 352,
    "fnof": 402,
    "scaron": 353,
    "Yuml": 376,
    "circ": 710,
    "tilde": 732,
    "Alpha": 913,
    "Beta": 914,
    "Gamma": 915,
    "Delta": 916,
    "Epsilon": 917,
    "Zeta": 918,
    "Eta": 919,
    "Theta": 920,
    "Iota": 921,
    "Kappa": 922,
    "Lambda": 923,
    "Mu": 924,
    "Nu": 925,
    "Xi": 926,
    "Omicron": 927,
    "Pi": 928,
    "Rho": 929,
    "Sigma": 931,
    "Tau": 932,
    "Upsilon": 933,
    "Phi": 934,
    "Chi": 935,
    "Psi": 936,
    "Omega": 937,
    "alpha": 945,
    "beta": 946,
    "gamma": 947,
    "delta": 948,
    "epsilon": 949,
    "zeta": 950,
    "eta": 951,
    "theta": 952,
    "iota": 953,
    "kappa": 954,
    "lambda": 955,
    "mu": 956,
    "nu": 957,
    "xi": 958,
    "omicron": 959,
    "pi": 960,
    "rho": 961,
    "sigmaf": 962,
    "sigma": 963,
    "tau": 964,
    "upsilon": 965,
    "phi": 966,
    "chi": 967,
    "psi": 968,
    "omega": 969,
    "thetasym": 977,
    "upsih": 978,
    "piv": 982,
    "bull": 8226,
    "hellip": 8230,
    "prime": 8242,
    "Prime": 8243,
    "oline": 8254,
    "frasl": 8260,
    "ensp": 8194,
    "emsp": 8195,
    "thinsp": 8201,
    "zwnj": 8204,
    "zwj": 8205,
    "lrm": 8206,
    "rlm": 8207,
    "ndash": 8211,
    "mdash": 8212,
    "lsquo": 8216,
    "rsquo": 8217,
    "sbquo": 8218,
    "ldquo": 8220,
    "rdquo": 8221,
    "bdquo": 8222,
    "dagger": 8224,
    "Dagger": 8225,
    "permil": 8240,
    "lsaquo": 8249,
    "rsaquo": 8250,
    "euro": 8364,
    "weierp": 8472,
    "image": 8465,
    "real": 8476,
    "trade": 8482,
    "alefsym": 8501,
    "larr": 8592,
    "uarr": 8593,
    "rarr": 8594,
    "darr": 8595,
    "harr": 8596,
    "crarr": 8629,
    "lArr": 8656,
    "uArr": 8657,
    "rArr": 8658,
    "dArr": 8659,
    "hArr": 8660,
    "forall": 8704,
    "part": 8706,
    "exist": 8707,
    "empty": 8709,
    "nabla": 8711,
    "isin": 8712,
    "notin": 8713,
    "ni": 8715,
    "prod": 8719,
    "sum": 8721,
    "minus": 8722,
    "lowast": 8727,
    "radic": 8730,
    "prop": 8733,
    "infin": 8734,
    "ang": 8736,
    "and": 8743,
    "or": 8744,
    "cap": 8745,
    "cup": 8746,
    "int": 8747,
    "there4": 8756,
    "sim": 8764,
    "cong": 8773,
    "asymp": 8776,
    "ne": 8800,
    "equiv": 8801,
    "le": 8804,
    "ge": 8805,
    "sub": 8834,
    "sup": 8835,
    "nsub": 8836,
    "sube": 8838,
    "supe": 8839,
    "oplus": 8853,
    "otimes": 8855,
    "perp": 8869,
    "sdot": 8901,
    "lceil": 8968,
    "rceil": 8969,
    "lfloor": 8970,
    "rfloor": 8971,
    "lang": 9001,
    "rang": 9002,
    "loz": 9674,
    "spades": 9824,
    "clubs": 9827,
    "hearts": 9829,
    "diams": 9830
}
