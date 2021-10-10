
pattern  = {
    # APA
    'BOOK' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'editor' : r'(?:.*บรรณาธิการ+.*)',
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)" ,
        'Book' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'Pim' : r"(?:(?:พิมพ์ครั้งที่[ ][0-9]+)?)",
        'translatefrom' : r'(?:แปลจาก+.*)',
        'translateby' : r'(?:ทรงแปลโดย+.*)',
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)",
        },
    'ARTICLE' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'editor' : r'(?:.*บรรณาธิการ+.*)',
        'Book' : r"",
        'Pim' : r"(?:(?:พิมพ์ครั้งที่[ ][0-9]+)?)",
        'NumPage' : r"(?:(?:[(]น\.\s[0-9]+\-[0-9]+[)]))",
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)",
    },
    'JOURNAL' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'magazine' : r"(?:[ก-์]+,+)",
        'numyear' : r"(?:[0-9]+[(][0-9]+[)])",
        'page' : r"(?:[0-9]+\-[0-9]+)"
    },
    'THESES':{
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'thesis' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'univer' : r"(?:[(](?:[ก-์]+\,\s[ก-์]+)*[)])"
    },
    'ELECTRONICS' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'article' : r'(?:([ก-์]|[A-Za-z])+\s?(?:(?:([ก-์]|[A-Za-z])+(?::)?(?:\s([ก-์]|[A-Za-z])+)?)|(?:\.\s([ก-์]|[A-Za-z])+(?:\s[a-zA-z]+)*\.(?:\s([ก-์]|[A-Za-z])+)*))(?:(?:\s\[([ก-์]|[A-Za-z])+\])|(?:\s\[[a-z A-Z]+\])))',
        'magazine' : r"(?:[ก-์]+)",
        'numyear' : r"(?:[0-9]+[(][0-9]+[)])",
        'page' : r"(?:[0-9]+\-[0-9]+)"
    },
    'WIKI' : {
        'subject' : r'^(?:[ก-์]+)',
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'day' : r"(?:สืบค้นเมื่อ\s[0-9]+\s[ก-์]+\s[0-9]+)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'web' : r"(?:\[[ก-์]+\])",
        'url' : r"(?:(?:สืบค้นจาก|จากวิกิพีเดีย)\s(?:https?:\/\/)?(?:[\w\-])+\.{1}(?:[a-zA-Z]{2,63})(?:[\/\w-]*)*\/?\??(?:[^#\n\r]*)?#?(?:[^\n\r]*)[^ ])"
    },

    # IEEE
    'PERIODICAL' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'article' : r"(?:\“[ก-์A-Za-z]+)",
        'magazine' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'numyear' : r"(?:ปีที่\s[0-9]+)",
        'numissue' : r"(?:ฉบับที่\s[0-9]+)",
        'page' : r"(?:หน้า\s[0-9]+\-[0-9]+)",
        'year' : r"(?:(?:\b\d{4}))"
    },
    'THESISIEEE' : {
        'Name' : r"([^ทรงแปลโดย])?((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'thesis' : r"(?:\“[ก-์]+)",
        'thesis1' : r"([วิทยานิพนธ์]+.(?:(?:[ก-์]+\.)*)?\s\(.[ก-์]+.\))",
        'uni' : r"(?:^[มหาวิทยาลัย][ก-์]+)",
        'city' : r"(?:[^มหาวิทยาลัย][ก-์]{0,30})",
        'year' : r"(?:(?:\b\d{4}))"
    },

    # HARVARD
    'JOURNALHARVARD' : {
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'year' : r"(?:(?:\b\d{4}))",
        'subject' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'magazine' : r"([ก-์]+)",
        'numyear' : r"(?:[0-9]+[(][0-9]+[)])",
        'page' : r"(?:หน้า\s[0-9]+\-[0-9]+)"
    },
    'BOOKHARVARD' : {
        'Name' : r"([^ทรงแปลโดย])?((?:[ก-์]{0,100}(,|)+\s([0-9]+)?[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'year' : r"(?:(?:\b\d{4}))",
        'Book' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+)|(?:([ก-์]|[A-Za-z]){30,100})|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)",
    },
    'ARTICLEHARVARD' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'year' : r"(?:(?:\b\d{4}))",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'editor' : r'(?:.*บรรณาธิการ+.*)',
        'Book' : r"",
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)",
    },
    'BOOKMANY' : {
        'Name' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'year' : r"(?:(?:\b\d{4}))",
        'title' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{0,100}(:)+.*)|(?:([ก-์]|[A-Za-z]))|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'Pim' : r"(?:(?:พิมพ์ครั้งที่[ ][0-9]+)?)",
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)[ ]+.*)",
    },
    'ELECTRONICSHARVARD' : {
        'Name' : r"(?:([ก-์])+\s([ก-์])+\:\s([ก-์])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]){0,})|(?:([ก-์])[^ ]+)",
        'year' : r"(?:(?:\b\d{4}))",
        'subject' : r"([ก-์]+,+)",
        'day' : r"(?:[0-9]+\s[ก-์]+\s[0-9]+)",
        'url' : r"(?:(?:https?:\/\/)?(?:[\w\-])+\.{1}(?:[a-zA-Z]{2,63})(?:[\/\w-]*)*\/?\??.{6})"
    },
    'THESISHARVARD' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'year' : r"(?:(?:\b\d{4}))",
        'thesis' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'degree' : r"(?:^[วิทยานิพนธ์][ก-์]+)",
        'uni' : r"(?:^[มหาวิทยาลัย][ก-์]+)",
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)"
    },

    # Vancouver
    'JOURNALARTICLES' : {
        'Name' : r"(.*?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        # 'article' : r"(?:[ก-์]{30,}\s?(?:[A-Za-z]\s[ก-์]+)?).",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:([ก-์]|[A-Z a-z]){30,100})|(?:([ก-์]|[A-Z- a-z])+\:\s[ก-์]+)|(([ก-์]|[A-Za-z])+\-([ก-์]|[A-Za-z])+.*)",
        'magazineyear' : r"(([ก-์]+)+\s?[0-9]*)",
        'numbook' : r"(?:[0-9]*)",
        'page' : r"(?:[0-9]+\-[0-9]+)"

    },
    'BOOKVANCOUVER' : {
        'Name' : r"((?:[ก-์]{0,30}(,|)+\s?[ก-๙A-Za-z\s]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*))",
        'Book' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:([ก-์]|[A-Z a-z]){30,100})|(?:([ไมเกรน]|[ECG])([ก-์]|[A-Za-z])+)",
        'Pim' : r"(?:(?:พิมพ์ครั้งที่[ ][0-9]+)?)",
        'Location' : r"(([ก-์]((\s+|\.)?)){0,60}(:)+)",
        'SamNakPim' : r"(?:([ก-์]((\s+|\.)?)){0,60}(;)+)",
        'year' : r"(?:(?:\b\d{4}))"
    },
    'THESISVANCOUVER' : {
        'Name' : r"(.*?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'title' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z]).*)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'Location' : r"(([ก-์]((\s+|\.)?)){0,60}(:)+)",
        'uni' : r"(?:([ก-์]((\s+|\.)?)){0,60}(;)+)",
        'year' : r"(?:(?:\b\d{4}))"
    },
    'INTERNET' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:([ก-์]|[A-Z a-z]){30,100})|(?:([ก-์]|[A-Z- a-z])+\:\s[ก-์]+)|(([ก-์]|[A-Za-z])+\-([ก-์]|[A-Za-z])+.*)",
        'magazine' : r"([ก-์]+\[[ก-์]+\])",
        'year' : r"(?:\b\d{4})",
        'access' : r"(?:\[[เข้าถึงเมื่อ\s[ก-๙0-9]+[ก-๙0-9]+\]\;)",
        'numyear' : r"(?:[0-9]+[(][0-9]+[)])",
        'page' : r"(?:\[หน้า\s[0-9]+\-[0-9]+\])",
        'url' : r"(?:(?:https?:\/\/)?(?:[\w\-])+\.{1}(?:[a-zA-Z]{2,63})(?:[\/\w-]*)*\/?\??(?:[^#\n\r]*)?#?(?:[^\n\r]*)\/)"
    },
    'HOMEPAGEWED' : {
        'home' : r"(?:[ก-์]+\s\[[ก-์]+\])",
        'Location' : r"(([ก-์]((\s+|\.)?)){0,60}(:)+)",
        'SamNakPim' : r"(([ก-์]((\s+|\.)?))+(;)+)",
        'year' : r"(?:[0-9]+.\[.*\])",
        'url' : r"(?:(?:เข้าถึงได้จาก\:\s)(?:https?:\/\/)?(?:[\w\-])+\.{1}(?:[a-zA-Z]{2,63})(?:[\/\w-]*)*\/?\??(?:[^#\n\r]*)?#?(?:[^\n\r]*)\/[a-z]+\.[a-z]+)"
    },
    'BLOG' : {
        'Name' : r"(.?[^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'nameblog' : r"(?:[A-Z \' a-zก-์]+\:\s[ก-์]+\s\[.*)",
        'Location' : r"(([ก-์]((\s+|\.)?)){0,60}(:)+)",
        'SamNakPim' : r"(?:([ก-์]((\s+|\.)?)){0,60}(;)+)",
        'year' : r"(?:\b\d{4})",
        'access' : r"(?:\[เข้าถึงเมื่อ\s[0-9]+\s[ก-์]+.*)",
        'url' : r"(?:(?:เข้าถึงได้จาก\:\s)(?:https?:\/\/)?(?:[\w\-])+\.{1}(?:[a-zA-Z]{2,63})(?:[\/\w-]*)*\/?\??(?:[^#\n\r]*)?#?(?:[^\n\r]*))"
    }
}
