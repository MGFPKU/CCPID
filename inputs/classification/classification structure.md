Level	Name	Chinese Name	Definition	Purpose in Dataset	Example
1	Category	类别	High-level classification based on the policy instrument’s operating mechanism	Provides overall structure and enables broad comparison across policy types	"Economic instruments; 
Regulatory instruments; 
Information instruments"
2	Group	组别	Functional grouping of instruments within each category	Organises instruments by regulatory function or policy logic	"Under regulatory instruments: 
Performance standards; 
Technology standards"
3	Approach	路径	A standardised and internationally comparable policy approach that groups instruments with similar design and regulatory logic	Core level for cross-country comparability	"Under performance standards:
Minimum Energy Performance Standards (MEPS) for electric appliances; 
Fuel economy standards"
4	Instrument	工具	A specific legal or regulatory measure implemented in a jurisdiction at a given time	Primary unit of observation in the dataset; reflects country-specific policy design	"Under MEPS for electric appliances:
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
6. For CCPID-specific groups or approaches, record their IFCMA correspondence (alignment status and reference approach) and the extension rationale to preserve international comparability.
7. Do not automatically include all green policies. Inclusion requires a credible GHG-affecting pathway; where the mitigation pathway is distant or unverified, keep the record but mark it for verification (needs_human_review) rather than assuming a mitigation effect.