# IFCMA Data Structure

Source: OECD (2024), *The IFCMA's Climate Policy Database: Policy Instruments Typology and Data Structure*, Section 3 and Annex C.

## Definition

A data structure is a coherent system that codifies information into organised data points. In the context of a policy database, it defines the unit of analysis and identifies the attributes necessary to classify, describe, and characterise policy instruments. It also provides definitions of attributes and response options and standardises response options where feasible. [Source: p. 14]

## Unit Of Analysis

The database is structured around the policy instrument, which is the primary unit of analysis. The database identifies policy instruments at a granular level and distinguishes them from broader policy packages. [Source: p. 14]

| Level | Description | Example | Source |
|---|---|---|---|
| Policy instrument | Primary unit of analysis. | A distinct standard, tax, subsidy, label, or public procurement rule. | p. 14 |
| Policy package | Broader framework that may contain several policy instruments. | A building code may include performance standards for windows or roofs and technology standards for heating systems. | p. 14 |
| Sub-scheme | Variation of the main policy instrument used to capture differentiated requirements, exemptions, refunds, transitional periods, compliance requirements, or enforcement mechanisms. | A CO2 emissions standard for motor vehicles with distinct requirements by vehicle class; a carbon tax with rates varying by fuel type. | p. 14; p. 34 |

## Matrix Structure

Each instrument and sub-scheme is described through policy attributes. In a matrix structure, policy instruments and sub-schemes are rows and attributes are columns. [Source: pp. 14-15]

| Row type | Attribute 1 | Attribute ... | Attribute i | Attribute n |
|---|---|---|---|---|
| Policy Instrument 1 | value | value | value | value |
| Sub-scheme 1: reduced rate | value | value | value | value |
| Sub-scheme m: exemption | value | value | value | value |
| Policy Instrument k | value | value | value | value |

Source: adapted from Table 2, p. 15.

## Attribute Blocs

The policy attributes are grouped into six thematic blocs. The first four blocs are raw policy data that can be sourced from legal statutes or regulations. Blocs five and six are derived by the IFCMA Secretariat based on specific methodologies. [Source: p. 15]

| Bloc | Name | Content | Data status | Source |
|---|---|---|---|---|
| 1 | Policy description | General information, name, description, stated objective, and policy package. | Raw policy data | p. 16 |
| 2 | Administrative information | Policy timeline, geographical scope, administrative level, jurisdiction, status, dates, authority, legal documents, and web links. | Raw policy data | p. 16 |
| 3 | Policy base and intensity | Policy base, regulated asset, regulated agent, regulated activity, and intensity. | Raw policy data | pp. 16-17 |
| 4 | Attributes specific to instrument types | Additional design and implementation attributes relevant to specific instrument types. | Raw policy data | pp. 17-18 |
| 5 | GHG emission base | Quantification of the GHG emissions the instrument covers through its policy structure. | Developed by Secretariat | p. 18 |
| 6 | Classification | Classification by IFCMA typology, sectors, GHG emissions source sectors, expected effect, GHGs, and energy carriers. | Developed by Secretariat | p. 18 |

## Priority Attributes

Annex C marks priority attributes with an asterisk. The paper states these priority attributes are necessary to conduct the GHG mapping and modelling envisioned under the IFCMA's technical work. [Source: p. 34]

| Bloc | Priority attributes shown in Annex C | Source |
|---|---|---|
| Policy description | Domestic instrument name; English instrument name; Policy package; Description. | pp. 34-35 |
| Administrative information | Country; Jurisdiction level; Jurisdiction name; Start date; Last revisions; Status; Legal document. | p. 35 |
| Policy regulatory base and intensity | Policy base; Intensity. | pp. 35-36 |
| Instrument-specific attributes | Subsidy level or rate; Earmarked revenue; Trading system type; Allowance mechanism; Compliance promotion. | pp. 36-37 |
| GHG emission base | GHG emission base. | p. 39 |
| Classification | Instrument Category; Instrument Type; Instrument; Economic sector; Emissions sector; GHGs affected. | pp. 39-40 |

## Attribute Examples

| Attribute | Definition or description | Variable type / response option | Source |
|---|---|---|---|
| Domestic instrument name | Instrument name in original language, preferably the commonly known name; if ambiguous, the name used in the legal statute. | Free text | p. 34 |
| English instrument name | Domestic instrument name translated to English. | Free text | p. 34 |
| Policy package | Overarching framework bundling multiple instruments to achieve synergistic effects, maximise impact, or minimise trade-offs. | Free text | p. 34 |
| Description | Brief description of the policy mechanism and specific design features. | Free text | p. 35 |
| Objective | Policy objective as stated in legislation. | Multiple choice, including climate change mitigation, adaptation, energy efficiency, air pollution, and other options. | p. 35 |
| Country | Country where the instrument is applied. | ISO 3-letter country code | p. 35 |
| Jurisdiction level | Jurisdiction level where the instrument is applied. | National; Sub-national; Supra-national | p. 35 |
| Status | Defines whether the instrument is active or inactive and whether it is in force. | In force; scheduled; ended | p. 35 |
| Legal statute | Relevant legal document(s), chapter(s), and/or article(s) establishing or modifying the instrument. | Free text | p. 35 |
| Legal document | Weblink to the relevant legal document. | Free text | p. 35 |
| Intensity | Legal obligation imposed on, or benefit provided for, the regulated agents. | Numerical; free where needed | p. 36 |
| GHG emission base | Total GHG emissions the instrument targets or potentially affects; defined by policy base and emission source. | Numerical | p. 39 |

## Instrument-Specific Attribute Examples

| Instrument type | Attribute examples | Source |
|---|---|---|
| Subsidies | Annual expenditure; subsidy level or rate; limit; distribution mechanism; enforcement mechanism; subsidy floor or ceiling. | p. 36 |
| Taxes | Earmarked revenue; annual revenue; annual revenue forgone. | p. 36 |
| Trading systems | Type; cap; allowance mechanism; revenue use; volume; linkages; market stabilisation mechanism; offset use allowed; penalties for non-compliance per unit. | p. 37 |
| Regulatory instruments | Compliance calculation methodology; compliance monitoring; compliance enforcement; compliance promotion. | pp. 37-38 |
| Public investment and procurement | Co-financing; selection process; tender process; award criteria; compliance monitoring; compliance enforcement; life-cycle costing. | p. 38 |
| Information instruments | Responsibility for information capturing; information transmission; frequency of information provision; public availability; label type; compliance monitoring; compliance enforcement; compliance promotion. | pp. 38-39 |
| Voluntary approaches | Incentives for participation; monitoring; sanctions for non-compliance. | p. 39 |

## Examples

| Data-structure concept | Example from paper | Source |
|---|---|---|
| Sub-scheme for differentiated requirements | Motor vehicle CO2 emissions standard with distinct performance requirements for each vehicle class. | p. 14 |
| Sub-scheme for exemption | Ambulances or military vehicles exempted from a motor vehicle policy. | p. 14 |
| Sub-scheme for varied rate | Carbon tax with rates varying by fuel type, represented by different regulated asset values and corresponding intensity. | p. 34 |
| Administrative phase | A policy implemented in phases, such as requirements becoming more stringent over time, entered as separate sub-schemes. | p. 16 |
| Intensity | Carbon tax rate per tonne of CO2e emitted; emission limit value for an emissions standard; feed-in-tariff payment per unit of renewable electricity generated. | p. 17 |

