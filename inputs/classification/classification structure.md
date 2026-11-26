Level	Name	Chinese Name	Definition	Purpose in Dataset	Example
1	Category	类别	High-level classification based on the policy instrument’s operating mechanism	Provides overall structure and enables broad comparison across policy types	"Economic instruments; 
Regulatory instruments; 
Information instruments"
2	Group	组别	Functional grouping of instruments within each category	Organises instruments by regulatory function or policy logic	"Under regulatory instruments: 
Performance standards; 
Technology standards"
3	Approach	路径	A standardised policy approach that groups instruments with similar operating mechanisms and policy design features, providing a basis for international comparison	Core level for cross-country comparability	"Under performance standards:
Minimum Energy Performance Standards (MEPS) for electric appliances; 
Fuel economy standards"
4	Instrument	工具	A specific policy measure, programme, scheme or rule implemented by public authorities in a jurisdiction at a given time, through which governments influence behaviour by imposing obligations, providing incentives or services, allocating resources, or providing information	Primary unit of observation in the dataset; reflects country-specific policy design	"Under MEPS for electric appliances:
MEPS for power transformer; 
MEPS for monitor; 
MEPS for air purifier"
5 (optional)	Sub-scheme	子方案	Variations within a single instrument reflecting differentiated requirements, exemptions, or implementation phases	Captures within-instrument heterogeneity when relevant	Efficiency tiers (e.g. Grade 1 / Grade 2); Phase-in periods

## Mixed-mechanism policy handling rules

1. Determine the main classification of an instrument by its primary legal obligation or direct incentive mechanism. Do not classify solely by policy name, competent authority, funding source, or policy objective.
2. When one policy document contains multiple measures with independent operating mechanisms, record the document as a policy package and split the measures into separate instruments. Do not force the whole document into one approach.
3. Use subschemes only for differentiation within one instrument (different agents, standards, rates, phases, or compliance conditions). When the legal obligations or operating mechanisms differ between parts, split into separate instruments instead.
4. Distinguish the government's own investment, procurement, and decision rules from regulatory obligations imposed on enterprises or projects. Whether the regulated entity is the government or a non-government agent determines the Government investment and consumption vs Regulatory category.
5. Voluntary participation does not imply the Voluntary approaches category. Distinguish voluntary project development, voluntary purchase, and voluntary trading participation from voluntary trading systems, government-issued offset credits, and mandatory compliance arrangements; the binding test is the operating mechanism and the legal obligation.
6. For CCPID-specific groups or approaches, record their IFCMA correspondence (alignment status) and the extension rationale to preserve international comparability. Do not force a correspondence for every CCPID approach: when no sufficiently accurate IFCMA reference exists, use CCPID-specific approach rather than an imperfect match.
7. Do not automatically include all green policies. Inclusion requires a credible GHG-affecting pathway; where the mitigation pathway is distant or unverified, keep the record but mark it for verification (needs_human_review) rather than assuming a mitigation effect.
8. When a parent instrument contains subschemes whose mitigation effects differ in direction or are uncertain, the parent instrument's Mitigation effect must not simply follow the judgement of any single class of subscheme; record it as Unknown (未知) unless the overall effect can be established.
9. Do not include policy documents whose sole function is to regulate the application, filing/recordation, approval, development and construction, engineering quality, safety management, acceptance, or day-to-day administration of green or low-carbon projects (排除一般性项目开发建设管理规定). Although such documents may facilitate low-carbon project development, their project-management function does not itself constitute a climate mitigation or mitigation-relevant policy instrument as defined by IFCMA. However, if a document also contains standalone policy instruments that meet this database's inclusion criteria — for example environmental permitting requirements, mandatory technical or performance standards, land-use regulations, renewable energy grid-connection and dispatch rules, or fiscal subsidies — identify and assess those instruments separately for inclusion, so that the whole document is not recorded again as a single instrument.