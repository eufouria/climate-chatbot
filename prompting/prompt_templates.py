project_prompt_template = """
Generate 12 alternative versions of the given project information to retrieve relevant 
documents from a vector database. Use the provided methodology details and project information 
to create diverse perspectives for similarity search. These variations should help overcome the 
limitations of distance-based similarity matching and ensure retrieval of the most relevant 
projects for creating a Project Description Document (PDD).

Inputs:
- Methodology: 
{methodology}
- Project Information: 
{project_information}

Objective:
Create alternative questions or reformulations of the user's project details to enhance document retrieval and address the following PDD components:
- Baseline conditions and reduction strategies.
- Project design and scope details.
- Sustainable development contributions.
- Risk assessment.
- Monitoring and verification procedures.
- Compliance with legal frameworks.
- Stakeholder engagement and consultation.
- GHG emission quantification and removal estimates.

Instructions:
- Provide 12 distinct alternative versions of the user's project information, separated by newlines.
"""

final_output_prompt_template = """
Generate a comprehensive **Project Description Document (PDD)** for a climate and environmental project based on the following inputs:

1. **User-Provided Project Information:**  
   {project_information}

2. **Retrieved Context from Registered and Validated Projects:**  
   {project_docs}

3. **Methodology Details:**  
   {method_docs}

**Follow this detailed template:**

1. Project Details
    1.1 Summary Description of the Project
        - Provide a summary description of the technologies/measures to be implemented by the project.
        - Explain how the project will generate GHG emission reductions or carbon dioxide removals.
        - Briefly describe the scenario existing prior to the project implementation.
        - Provide an estimate of annual average and total reductions and removals.
    1.2 Audit History
        - Include the audit history of the project (validation/verification dates and details).
    1.3 Sectoral Scope and Project Type
        - Identify the sectoral scope and project type.
    1.4 Project Eligibility
        - Justify project eligibility under the VCS Program, including methodology applicability and compliance.
    1.5 Project Design
        - State if the project is single location, multiple locations, or a grouped project.
    1.6 Project Proponent
        - Provide contact details for the project proponent(s).
    1.7 Other Entities Involved in the Project
        - Include roles and responsibilities of other entities involved.
    1.8 Ownership
        - Provide evidence of project ownership.
    1.9 Project Start Date
        - Indicate the project start date and justification for compliance.
    1.10 Project Crediting Period
        - Specify crediting period (e.g., seven years, twice renewable, or ten years fixed).
    1.11 Project Scale and Estimated GHG Emission Reductions or Removals
        - Indicate project scale and estimated GHG reductions/removals.
    1.12 Description of the Project Activity
        - Detail the project activities, technologies, and measures.
    1.13 Project Location
        - Provide the geographic boundaries, including geodetic coordinates.
    1.14 Conditions Prior to Project Initiation
        - Describe baseline conditions and demonstrate no generation of emissions for reduction purposes.
    1.15 Compliance with Laws, Statutes, and Other Regulatory Frameworks
        - Identify and demonstrate project compliance with relevant legal frameworks.
    1.16 Double Counting and Participation under Other GHG Programs
        - Ensure no double issuance or claiming and compliance with other GHG program requirements.
    1.17 Double Claiming, Other Forms of Credit, and Scope 3 Emissions
        - Address double claiming with emissions trading programs and other environmental credit systems.
    1.18 Sustainable Development Contributions
        - Explain how the project contributes to sustainable development.
    1.19 Additional Information Relevant to the Project
        - Include leakage management and any other relevant information.

2. Safeguards and Stakeholder Engagement
    2.1 Stakeholder Engagement and Consultation
        - Describe stakeholder identification, consultation processes, and outcomes.
    2.2 Risks to Stakeholders and the Environment
        - Conduct a risk assessment and outline mitigation measures.
    2.3 Respect for Human Rights and Equity
        - Address labor and human rights risks and mitigation.
    2.4 Ecosystem Health
        - Identify risks related to biodiversity, soil erosion, and water consumption.

3. Application of Methodology
    For this section, utilized the methodology details provided above. Provide details
    of formulas, calculations examples, and assumptions based on the equations and information provided in the methodology.
    3.1 Title and Reference of Methodology
        - Provide the title, reference, and version of the applied methodology.
    3.2 Applicability of Methodology
        - Provide details of applicability and compliance with the methodology based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    3.3 Project Boundary
        - Provide details of projection with the methodology based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    3.4 Baseline Scenario
        - Provide and justify the baseline scenario based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    3.5 Additionality
        - Demonstrate project additionality based on the methodology information provided above.
    3.6 Methodology Deviations
        - Describe and justify any methodology deviations based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.

4. Quantification of Estimated GHG Emission Reductions and Removals
    For this section, utilized the methodology details provided above. Provide details
    of formulas, calculations examples, and assumptions based on the equations and information provided in the methodology.
    4.1 Baseline Emissions
        - Describe quantification of baseline emissions or carbon stock changes based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    4.2 Project Emissions
        - Outline procedures for quantification of project emissions based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    4.3 Leakage Emissions
        - Describe procedures for quantifying leakage emissions based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    4.4 Estimated GHG Emission Reductions and Carbon Dioxide Removals
        - Quantify GHG reductions/removals and document calculations based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.

5. Monitoring
    5.1 Data and Parameters Available at Validation
        - Detail data and parameters determined at validation.
    5.2 Data and Parameters Monitored
        - Specify monitored data and parameters during project operation.
    5.3 Monitoring Plan
        - Describe processes and schedules for data monitoring and management.

At each section, write with your best effort and provide as much information as possible for user.

Instructions:
- Use as much details as possible for each section based on the inputs provided.
- Ensure clarity and precision, particularly in technical and compliance-related sections.
- Align the content with the user's project information and the retrieved documents.
- Provide details or recommendations that are relevant to the user's project.
- Provide formulas, examples and calculations where necessary, refer to the methodology details for guidance and information of the project.
- Utilize the methodology details to ensure compliance with the methodology requirements.
"""


methodology_prompt_template = """
Given the project information below, identify the methodology used in this project:\n
{project_information}\n
Provide a concise name code, if the code is unavailable, recommend a methodology that best fits the project information. 

Here is the list of active methodology that could be used:
ACM0001: Flaring or use of landfill gas
ACM0002: Grid-connected electricity generation from renewable sources
ACM0003: Partial substitution of fossil fuels in cement or quicklime manufacture
ACM0006: Electricity and heat generation from biomass
ACM0007: Conversion from single cycle to combined cycle power generation
ACM0008: Abatement of methane from coal mines
ACM0009: Fuel switching from coal or petroleum fuel to natural gas
ACM0010: GHG emission reductions from manure management systems 
must be used with Clarification issued on July 5, 2024
ACM0011: Fuel switching from coal and/or petroleum fuels to natural gas in existing power plants for electricity generation
ACM0012: Waste energy recovery
ACM0014: Treatment of wastewater 
ACM0016: Mass Rapid Transit Projects
ACM0017: Production of biofuel
ACM0018: Electricity generation from biomass in power-only plants
ACM0022: Alternative waste treatment processes
AM0009: Recovery and utilization of gas from oil fields that would otherwise be flared or vented
AM0023: Leak detection and repair in gas production, processing, transmission, storage and distribution systems and in refinery facilities
AM0026: Methodology for zero-emissions grid-connected electricity generation from renewable sources in Chile or in countries with merit order based dispatch grid
AM0028: N2O destruction in the tail gas of Caprolactam production plants
AM0036: Use of biomass in heat generation equipment
AM0059: Reduction in GHGs emission from primary aluminium smelters
AM0064: Capture and utilisation or destruction of mine methane (excluding coal mines) or non mine methane
AM0070: Manufacturing of energy efficient domestic refrigerators
AM0072: Fossil Fuel Displacement by Geothermal Resources for Space Heating
AM0073 – GHG Emission Reductions Through Multi-site Manure Collection and Treatment in a Central Plan
must be used with C&C AM0073 (18July2024) (see announcement)
AM0080: Mitigation of greenhouse gases emissions with treatment of wastewater in aerobic wastewater treatment plants
AM0090: Modal shift in transportation of cargo from road transportation to water or rail transportation
AM0124: Hydrogen production from electrolysis of water
AMS-I.B.: Mechanical energy for the user with or without electrical energy
AMS-I.C.: Thermal energy production with or without electricity
AMS-I.D.: Grid connected renewable electricity generation
AMS-I.F.: Renewable electricity generation for captive use and mini-grid
AMS-I.L.: Electrification of rural communities using renewable energy
AMS-II.C.: Demand-side energy efficiency activities for specific technologies
AMS-II.D.: Energy efficiency and fuel switching measures for industrial facilities
AMS-II.J.: Demand-side activities for efficient lighting technologies
AMS-II.S.: Energy efficiency in motor systems
must be used with the Clarification issued on December 19, 2023
AMS-III.AO.: Methane recovery through controlled anaerobic digestion
AMS-III.AQ.: Introduction of Bio-CNG in transportation applications
AMS-III.AR.: Substituting fossil fuel based lighting with LED/CFL lighting systems
AMS-III.AV.: Low greenhouse gas emitting safe drinking water production systems
AMS-III.B.: Switching fossil fuels
AMS-III.BM.: Lightweight two and three wheeled personal transportation
AMS-III.C.: Emission reductions by electric and hybrid vehicles
AMS-III.D.: Methane recovery in animal manure management systems
must be used with Clarification issued on July 5, 2024
AMS-III.E.: Avoidance of methane production from decay of biomass through controlled combustion, gasification or mechanical/thermal treatment
AMS-III.F.: Avoidance of methane emissions through composting
AMS-III.G.: Landfill methane recovery
AMS-III.H.: Methane recovery in wastewater treatment
AMS-III.I.: Avoidance of methane production in wastewater treatment through replacement of anaerobic systems by aerobic systems
must be used with Clarification issued on July 5, 2024
AMS-III.Q.: Waste energy recovery
AMS-III.Y.: Methane avoidance through separation of solids from wastewater or manure treatment systems
must be used with Clarification issued on July 5, 2024
AMS-III.Z.: Fuel Switch, process improvement and energy efficiency in brick manufacture
VM0001 Refrigerant Leak Detection, v1.2
VM0003 Methodology for Improved Forest Management through Extension of Rotation Age, v1.3
VM0005 Methodology for Conversion of Low-Productive Forest to High-Productive Forest, v1.2
VM0006 Methodology for Carbon Accounting for Mosaic and Landscape-scale REDD Projects, v2.2
VM0007 REDD+ Methodology Framework (REDD-MF), v1.7
VM0008 Weatherization of Single-Family and Multi-Family Buildings, v1.1
VM0010 Methodology for Improved Forest Management: Conversion from Logged to Protected Forest, v1.4
VM0011 Methodology for Calculating GHG Benefits from Preventing Planned Degradation, v1.0
VM0012 Improved Forest Management in Temperate and Boreal Forests (LtPF), v1.2
VM0015 Methodology for Avoided Unplanned Deforestation, v1.1
VM0016 Recovery and Destruction of Ozone-Depleting Substances (ODS) from Products, v1.1
VM0018 Energy Efficiency and Solid Waste Diversion Activities within a Sustainable Community, v1.0
VM0019 Fuel Switch from Gasoline to Ethanol in Flex-Fuel Vehicle Fleets, v1.0
VM0025 Campus Clean Energy and Energy Efficiency, v1.0
VM0032 Methodology for the Adoption of Sustainable Grasslands through Adjustment of Fire and Grazing, v1.0
VM0033 Methodology for Tidal Wetland and Seagrass Restoration, v2.1
VM0034 Canadian Forest Carbon Offset Methodology, v2.0
VM0035 Methodology for Improved Forest Management through Reduced Impact Logging v1.0
VM0036 Methodology for Rewetting Drained Temperate Peatlands, v1.0
VM0038 Methodology for Electric Vehicle Charging Systems, v1.0
VM0039 Methodology for Use of Foam Stabilized Base and Emulsion Asphalt Mixtures in Pavement Application, v1.0
VM0041 Methodology for the Reduction of Enteric Methane Emissions from Ruminants through the Use of Feed Ingredients, v2.0
VM0042 Improved Agricultural Land Management, v2.1
VM0043 Methodology for CO2 Utilization in Concrete Production, v1.0
VM0044 Methodology for Biochar Utilization in Soil and Non-Soil Applications, v1.1
VM0045 Improved Forest Management Methodology Using Dynamic Matched Baselines from National Forest Inventories, v1.0
VM0046 Methodology for Reducing Food Loss and Waste, v1.0
VM0047 Afforestation, Reforestation, and Revegetation, v1.0
VM0048 Reducing Emissions from Deforestation and Forest Degradation, v1.0
VM0049 Carbon Capture and Storage
VM0050 Energy Efficiency and Fuel-Switch Measures in Cookstoves, v1.0
VMR0004 Improved Efficiency of Fleet Vehicles, v2.0
VMR0007 Revision to AMS-III.AJ.: Recovery and Recycling of Materials from Solid Wastes, v1.0
VMR0008 Revision to AMS-III.BA.: Recovery and Recycling of Materials from E-waste, v1.0
VMR0009 Revision to AM0057: Avoided Emissions from Biomass Wastes through Use as Feed stock in Pulp and Paper, Cardboard, Fiberboard or Bio-oil Production, v1.0
VMR0010 Electricity Supply for Ships, v1.0
VMR0012 Production of Geopolymer Cement, v1.0"""

qa_query_prompt_template = """
Generate 10 alternative versions of the given project information and question to retrieve relevant 
documents from a vector database. Use the provided methodology details and project information 
to create diverse perspectives for similarity search. These variations should help overcome the 
limitations of distance-based similarity matching and ensure retrieval of the most relevant 
projects for creating a Project Description Document (PDD).

Inputs:
- Question: 
{question}
- Project Information: 
{project_information}

Instructions:
- Provide 10 distinct alternative versions of the user's project information, separated by newlines.
"""

qa_prompt_template = """
You are Climate AI Assistant. You have been asked to provide a detailed response to the following 
question based on the user's project information and retrieval data provided. Provide a detailed and relevant content only.
If the information is outside of the retrieval data, you can generate a response based on the data you are trained on.

Question: {question}
Project Information: {project_information}
Retrieval Data: {retrieval_docs}

Besides, here is the list of active methodology that could be used, the methodology other than the list cannot be used since 
they are invalid or unactive. Only refer to this if you need to:

ACM0001: Flaring or use of landfill gas
ACM0002: Grid-connected electricity generation from renewable sources
ACM0003: Partial substitution of fossil fuels in cement or quicklime manufacture
ACM0006: Electricity and heat generation from biomass
ACM0007: Conversion from single cycle to combined cycle power generation
ACM0008: Abatement of methane from coal mines
ACM0009: Fuel switching from coal or petroleum fuel to natural gas
ACM0010: GHG emission reductions from manure management systems 
must be used with Clarification issued on July 5, 2024
ACM0011: Fuel switching from coal and/or petroleum fuels to natural gas in existing power plants for electricity generation
ACM0012: Waste energy recovery
ACM0014: Treatment of wastewater 
ACM0016: Mass Rapid Transit Projects
ACM0017: Production of biofuel
ACM0018: Electricity generation from biomass in power-only plants
ACM0022: Alternative waste treatment processes
AM0009: Recovery and utilization of gas from oil fields that would otherwise be flared or vented
AM0023: Leak detection and repair in gas production, processing, transmission, storage and distribution systems and in refinery facilities
AM0026: Methodology for zero-emissions grid-connected electricity generation from renewable sources in Chile or in countries with merit order based dispatch grid
AM0028: N2O destruction in the tail gas of Caprolactam production plants
AM0036: Use of biomass in heat generation equipment
AM0059: Reduction in GHGs emission from primary aluminium smelters
AM0064: Capture and utilisation or destruction of mine methane (excluding coal mines) or non mine methane
AM0070: Manufacturing of energy efficient domestic refrigerators
AM0072: Fossil Fuel Displacement by Geothermal Resources for Space Heating
AM0073: GHG Emission Reductions Through Multi-site Manure Collection and Treatment in a Central Plan
must be used with C&C AM0073 (18July2024) (see announcement)
AM0080: Mitigation of greenhouse gases emissions with treatment of wastewater in aerobic wastewater treatment plants
AM0090: Modal shift in transportation of cargo from road transportation to water or rail transportation
AM0124: Hydrogen production from electrolysis of water
AMS-I.B.: Mechanical energy for the user with or without electrical energy
AMS-I.C.: Thermal energy production with or without electricity
AMS-I.D.: Grid connected renewable electricity generation
AMS-I.F.: Renewable electricity generation for captive use and mini-grid
AMS-I.L.: Electrification of rural communities using renewable energy
AMS-II.C.: Demand-side energy efficiency activities for specific technologies
AMS-II.D.: Energy efficiency and fuel switching measures for industrial facilities
AMS-II.J.: Demand-side activities for efficient lighting technologies
AMS-II.S.: Energy efficiency in motor systems
must be used with the Clarification issued on December 19, 2023
AMS-III.AO.: Methane recovery through controlled anaerobic digestion
AMS-III.AQ.: Introduction of Bio-CNG in transportation applications
AMS-III.AR.: Substituting fossil fuel based lighting with LED/CFL lighting systems
AMS-III.AV.: Low greenhouse gas emitting safe drinking water production systems
AMS-III.B.: Switching fossil fuels
AMS-III.BM.: Lightweight two and three wheeled personal transportation
AMS-III.C.: Emission reductions by electric and hybrid vehicles
AMS-III.D.: Methane recovery in animal manure management systems
must be used with Clarification issued on July 5, 2024
AMS-III.E.: Avoidance of methane production from decay of biomass through controlled combustion, gasification or mechanical/thermal treatment
AMS-III.F.: Avoidance of methane emissions through composting
AMS-III.G.: Landfill methane recovery
AMS-III.H.: Methane recovery in wastewater treatment
AMS-III.I.: Avoidance of methane production in wastewater treatment through replacement of anaerobic systems by aerobic systems
must be used with Clarification issued on July 5, 2024
AMS-III.Q.: Waste energy recovery
AMS-III.Y.: Methane avoidance through separation of solids from wastewater or manure treatment systems
must be used with Clarification issued on July 5, 2024
AMS-III.Z.: Fuel Switch, process improvement and energy efficiency in brick manufacture
VM0001 Refrigerant Leak Detection, v1.2
VM0003 Methodology for Improved Forest Management through Extension of Rotation Age, v1.3
VM0005 Methodology for Conversion of Low-Productive Forest to High-Productive Forest, v1.2
VM0006 Methodology for Carbon Accounting for Mosaic and Landscape-scale REDD Projects, v2.2
VM0007 REDD+ Methodology Framework (REDD-MF), v1.7
VM0008 Weatherization of Single-Family and Multi-Family Buildings, v1.1
VM0010 Methodology for Improved Forest Management: Conversion from Logged to Protected Forest, v1.4
VM0011 Methodology for Calculating GHG Benefits from Preventing Planned Degradation, v1.0
VM0012 Improved Forest Management in Temperate and Boreal Forests (LtPF), v1.2
VM0015 Methodology for Avoided Unplanned Deforestation, v1.1
VM0016 Recovery and Destruction of Ozone-Depleting Substances (ODS) from Products, v1.1
VM0018 Energy Efficiency and Solid Waste Diversion Activities within a Sustainable Community, v1.0
VM0019 Fuel Switch from Gasoline to Ethanol in Flex-Fuel Vehicle Fleets, v1.0
VM0025 Campus Clean Energy and Energy Efficiency, v1.0
VM0032 Methodology for the Adoption of Sustainable Grasslands through Adjustment of Fire and Grazing, v1.0
VM0033 Methodology for Tidal Wetland and Seagrass Restoration, v2.1
VM0034 Canadian Forest Carbon Offset Methodology, v2.0
VM0035 Methodology for Improved Forest Management through Reduced Impact Logging v1.0
VM0036 Methodology for Rewetting Drained Temperate Peatlands, v1.0
VM0038 Methodology for Electric Vehicle Charging Systems, v1.0
VM0039 Methodology for Use of Foam Stabilized Base and Emulsion Asphalt Mixtures in Pavement Application, v1.0
VM0041 Methodology for the Reduction of Enteric Methane Emissions from Ruminants through the Use of Feed Ingredients, v2.0
VM0042 Improved Agricultural Land Management, v2.1
VM0043 Methodology for CO2 Utilization in Concrete Production, v1.0
VM0044 Methodology for Biochar Utilization in Soil and Non-Soil Applications, v1.1
VM0045 Improved Forest Management Methodology Using Dynamic Matched Baselines from National Forest Inventories, v1.0
VM0046 Methodology for Reducing Food Loss and Waste, v1.0
VM0047 Afforestation, Reforestation, and Revegetation, v1.0
VM0048 Reducing Emissions from Deforestation and Forest Degradation, v1.0
VM0049 Carbon Capture and Storage
VM0050 Energy Efficiency and Fuel-Switch Measures in Cookstoves, v1.0
VMR0004 Improved Efficiency of Fleet Vehicles, v2.0
VMR0007 Revision to AMS-III.AJ.: Recovery and Recycling of Materials from Solid Wastes, v1.0
VMR0008 Revision to AMS-III.BA.: Recovery and Recycling of Materials from E-waste, v1.0
VMR0009 Revision to AM0057: Avoided Emissions from Biomass Wastes through Use as Feed stock in Pulp and Paper, Cardboard, Fiberboard or Bio-oil Production, v1.0
VMR0010 Electricity Supply for Ships, v1.0
VMR0012 Production of Geopolymer Cement, v1.0

At each section, write with your best effort and provide as much information as possible for user.

Instructions:
- Use as much details as possible for each section based on the inputs provided.
- Ensure clarity and precision, particularly in technical and compliance-related sections.
- Align the content with the user's project information and the retrieved documents.
- Provide details or recommendations that are relevant to the user's project.
- Provide formulas, examples and calculations where necessary, refer to the methodology details for guidance and information of the project.
- Utilize the methodology details to ensure compliance with the methodology requirements.
"""


final_output_prompt_template = """
Generate a comprehensive **Project Description Document (PDD)** for a climate and environmental project based on the following inputs:

1. **User-Provided Project Information:**  
   {project_information}

2. **Retrieved Context from Registered and Validated Projects:**  
   {project_docs}

3. **Methodology Details:**  
   {method_docs}

**Follow this detailed template:**

1. Project Details
    1.1 Summary Description of the Project
        - Provide a summary description of the technologies/measures to be implemented by the project.
        - Explain how the project will generate GHG emission reductions or carbon dioxide removals.
        - Briefly describe the scenario existing prior to the project implementation.
        - Provide an estimate of annual average and total reductions and removals.
    1.2 Audit History
        - Include the audit history of the project (validation/verification dates and details).
    1.3 Sectoral Scope and Project Type
        - Identify the sectoral scope and project type.
    1.4 Project Eligibility
        - Justify project eligibility under the VCS Program, including methodology applicability and compliance.
    1.5 Project Design
        - State if the project is single location, multiple locations, or a grouped project.
    1.6 Project Proponent
        - Provide contact details for the project proponent(s).
    1.7 Other Entities Involved in the Project
        - Include roles and responsibilities of other entities involved.
    1.8 Ownership
        - Provide evidence of project ownership.
    1.9 Project Start Date
        - Indicate the project start date and justification for compliance.
    1.10 Project Crediting Period
        - Specify crediting period (e.g., seven years, twice renewable, or ten years fixed).
    1.11 Project Scale and Estimated GHG Emission Reductions or Removals
        - Indicate project scale and estimated GHG reductions/removals.
    1.12 Description of the Project Activity
        - Detail the project activities, technologies, and measures.
    1.13 Project Location
        - Provide the geographic boundaries, including geodetic coordinates.
    1.14 Conditions Prior to Project Initiation
        - Describe baseline conditions and demonstrate no generation of emissions for reduction purposes.
    1.15 Compliance with Laws, Statutes, and Other Regulatory Frameworks
        - Identify and demonstrate project compliance with relevant legal frameworks.
    1.16 Double Counting and Participation under Other GHG Programs
        - Ensure no double issuance or claiming and compliance with other GHG program requirements.
    1.17 Double Claiming, Other Forms of Credit, and Scope 3 Emissions
        - Address double claiming with emissions trading programs and other environmental credit systems.
    1.18 Sustainable Development Contributions
        - Explain how the project contributes to sustainable development.
    1.19 Additional Information Relevant to the Project
        - Include leakage management and any other relevant information.

2. Safeguards and Stakeholder Engagement
    2.1 Stakeholder Engagement and Consultation
        - Describe stakeholder identification, consultation processes, and outcomes.
    2.2 Risks to Stakeholders and the Environment
        - Conduct a risk assessment and outline mitigation measures.
    2.3 Respect for Human Rights and Equity
        - Address labor and human rights risks and mitigation.
    2.4 Ecosystem Health
        - Identify risks related to biodiversity, soil erosion, and water consumption.

3. Application of Methodology
    For this section, utilized the methodology details provided above. Provide details
    of formulas, calculations examples, and assumptions based on the equations and information provided in the methodology.
    3.1 Title and Reference of Methodology
        - Provide the title, reference, and version of the applied methodology.
    3.2 Applicability of Methodology
        - Provide details of applicability and compliance with the methodology based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    3.3 Project Boundary
        - Provide details of projection with the methodology based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    3.4 Baseline Scenario
        - Provide and justify the baseline scenario based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    3.5 Additionality
        - Demonstrate project additionality based on the methodology information provided above.
    3.6 Methodology Deviations
        - Describe and justify any methodology deviations based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.

4. Quantification of Estimated GHG Emission Reductions and Removals
    For this section, utilized the methodology details provided above. Provide details
    of formulas, calculations examples, and assumptions based on the equations and information provided in the methodology.
    4.1 Baseline Emissions
        - Describe quantification of baseline emissions or carbon stock changes based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    4.2 Project Emissions
        - Outline procedures for quantification of project emissions based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    4.3 Leakage Emissions
        - Describe procedures for quantifying leakage emissions based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.
    4.4 Estimated GHG Emission Reductions and Carbon Dioxide Removals
        - Quantify GHG reductions/removals and document calculations based on the methodology information provided above.
        Write about this section with your best effort and provide as much information as possible for user.

5. Monitoring
    5.1 Data and Parameters Available at Validation
        - Detail data and parameters determined at validation.
    5.2 Data and Parameters Monitored
        - Specify monitored data and parameters during project operation.
    5.3 Monitoring Plan
        - Describe processes and schedules for data monitoring and management.

At each section, write with your best effort and provide as much information as possible for user.

Instructions:
- Use as much details as possible for each section based on the inputs provided.
- Ensure clarity and precision, particularly in technical and compliance-related sections.
- Align the content with the user's project information and the retrieved documents.
- Provide details or recommendations that are relevant to the user's project.
- Provide formulas, examples and calculations where necessary, refer to the methodology details for guidance and information of the project.
- Utilize the methodology details to ensure compliance with the methodology requirements.
"""


final_output_prompt_template2 = """
Generate a comprehensive **Project Description Document (PDD)** for a climate and environmental project based on the following inputs:

1. **User-Provided Project Information:**  
   {project_information}

2. **Retrieved Context from Registered and Validated Projects:**  
   {project_docs}

3. **Methodology Details:**  
   {method_docs}

**Follow this detailed template:**

1. Project Details
    1.1 Summary Description of the Project
        - Provide a summary description of the technologies/measures to be implemented by the project.
        - Explain how the project will generate GHG emission reductions or carbon dioxide removals.
        - Briefly describe the scenario existing prior to the project implementation.
        - Provide an estimate of annual average and total reductions and removals.
    1.2 Audit History
        - Include the audit history of the project (validation/verification dates and details).
    1.3 Sectoral Scope and Project Type
        - Identify the sectoral scope and project type.
    1.4 Project Eligibility
        - Justify project eligibility under the VCS Program, including methodology applicability and compliance.
    1.5 Project Design
        - State if the project is single location, multiple locations, or a grouped project.
    1.6 Project Proponent
        - Provide contact details for the project proponent(s).
    1.7 Other Entities Involved in the Project
        - Include roles and responsibilities of other entities involved.
    1.8 Ownership
        - Provide evidence of project ownership.
    1.9 Project Start Date
        - Indicate the project start date and justification for compliance.
    1.10 Project Crediting Period
        - Specify crediting period (e.g., seven years, twice renewable, or ten years fixed).
    1.11 Project Scale and Estimated GHG Emission Reductions or Removals
        - Indicate project scale and estimated GHG reductions/removals.
    1.12 Description of the Project Activity
        - Detail the project activities, technologies, and measures.
    1.13 Project Location
        - Provide the geographic boundaries, including geodetic coordinates.
    1.14 Conditions Prior to Project Initiation
        - Describe baseline conditions and demonstrate no generation of emissions for reduction purposes.
    1.15 Compliance with Laws, Statutes, and Other Regulatory Frameworks
        - Identify and demonstrate project compliance with relevant legal frameworks.
    1.16 Double Counting and Participation under Other GHG Programs
        - Ensure no double issuance or claiming and compliance with other GHG program requirements.
    1.17 Double Claiming, Other Forms of Credit, and Scope 3 Emissions
        - Address double claiming with emissions trading programs and other environmental credit systems.
    1.18 Sustainable Development Contributions
        - Explain how the project contributes to sustainable development.
    1.19 Additional Information Relevant to the Project
        - Include leakage management and any other relevant information.

2. Safeguards and Stakeholder Engagement
    2.1 Stakeholder Engagement and Consultation
        - Describe stakeholder identification, consultation processes, and outcomes.
    2.2 Risks to Stakeholders and the Environment
        - Conduct a risk assessment and outline mitigation measures.
    2.3 Respect for Human Rights and Equity
        - Address labor and human rights risks and mitigation.
    2.4 Ecosystem Health
        - Identify risks related to biodiversity, soil erosion, and water consumption.

3. Application of Methodology
    3.1 Title and Reference of Methodology
        - Provide the title, reference, and version of the applied methodology.
    3.2 Applicability of Methodology
        - Provide details of applicability and compliance with the methodology based on the methodology information provided above.
    3.3 Project Boundary
        - Provide details of projection with the methodology based on the methodology information provided above.
    3.4 Baseline Scenario
        - Provide and justify the baseline scenario based on the methodology information provided above.
    3.5 Additionality
        - Demonstrate project additionality based on the methodology information provided above.
    3.6 Methodology Deviations
        - Describe and justify any methodology deviations based on the methodology information provided above.

4. Quantification of Estimated GHG Emission Reductions and Removals
    4.1 Baseline Emissions
        - Describe quantification of baseline emissions or carbon stock changes based on the methodology information provided above.
    4.2 Project Emissions
        - Outline procedures for quantification of project emissions based on the methodology information provided above.
    4.3 Leakage Emissions
        - Describe procedures for quantifying leakage emissions based on the methodology information provided above.
    4.4 Estimated GHG Emission Reductions and Carbon Dioxide Removals
        - Quantify GHG reductions/removals and document calculations based on the methodology information provided above.

5. Monitoring
    5.1 Data and Parameters Available at Validation
        - Detail data and parameters determined at validation.
    5.2 Data and Parameters Monitored
        - Specify monitored data and parameters during project operation.
    5.3 Monitoring Plan
        - Describe processes and schedules for data monitoring and management.
"""

