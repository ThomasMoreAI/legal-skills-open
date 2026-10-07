# Topic → Search Term Reference

Map colloquial legal topics to effective `legal-ko-cli search` terms.
Run **all listed terms** for the matching topic.

| Topic (Korean) | Topic (English) | Search Terms |
|----------------|-----------------|--------------|
| 전세, 월세, 임대차 | Lease, rent, jeonse | `임대차`, `주택`, `민법`, `보증금` |
| 부동산 매매 | Real estate | `부동산`, `등기`, `공인중개사`, `민법` |
| 이혼, 양육권 | Divorce, custody | `민법`, `가사소송`, `가정폭력`, `양육` |
| 상속, 유언 | Inheritance, wills | `민법`, `상속세`, `유언` |
| 노동, 근로, 해고 | Labor, employment | `근로기준`, `노동조합`, `최저임금`, `고용` |
| 교통사고 | Traffic accident | `도로교통`, `자동차손해`, `교통사고` |
| 사기, 범죄, 폭행 | Fraud, crime, assault | `형법`, `형사소송`, `특정범죄` |
| 소비자 피해, 환불 | Consumer, refund | `소비자`, `전자상거래`, `할부거래` |
| 개인정보 | Privacy, data | `개인정보`, `정보통신`, `신용정보` |
| 회사, 창업, 법인 | Company, startup | `상법`, `중소기업`, `벤처`, `법인세` |
| 의료 사고 | Medical malpractice | `의료`, `민법`, `형법` |
| 지식재산, 저작권 | IP, copyright | `저작권`, `특허`, `상표`, `부정경쟁` |
| 군대, 병역 | Military service | `병역`, `군형법`, `군인` |
| 세금, 납세 | Tax | `소득세`, `부가가치세`, `법인세`, `국세` |
| 행정 처분 | Administrative | `행정`, `인허가`, `행정소송`, `행정절차` |
| 환경, 소음 | Environment, noise | `환경`, `소음`, `폐기물` |
| 학교, 교육 | Education | `교육`, `학교`, `학원` |

> If the topic doesn't appear above, decompose into underlying legal concepts.
> Korean law names are descriptive — a keyword usually appears in the title.

## Law Category Hierarchy

| Level | Category | Description |
|-------|----------|-------------|
| 1 | `법률` | Acts (국회) |
| 2 | `대통령령` (시행령) | Presidential decrees |
| 3 | `부령` (시행규칙) | Ministerial regulations |

Start with `법률`; drill into `대통령령`/`부령` only for implementation details.
