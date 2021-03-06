# Explainable-Stall-AI
DESIGN OF A COMPLIMENTARY MACHINE LEARNING AERODYNAMIC STALL WARNING

**Team Machine:**
Sean Case,
Jake Ryan,
Adam Ferguson,
and Ajay Kurian



**Abstract:** Aerodynamic stall events are fairly rare events where influxes of turbulence reduces the flight-enabling lift force for a plane, leading to an airline crash. This project aims to create a complimentary Artificial Intelligence (AI) Stall Warning model based on Machine Learning (ML) from historic flight data. The models could significantly increase safety margins for the stall hazard by identifying the onset of stall reliably before a human operator could. The models utilize simulated flight data as a proxy for historical flight data parameters, housed within an AWS SageMaker Jupyter Notebook. The two models we researched were anomaly detection through a Random Cut Forest and a predictive LSTM model from AWS SageMaker DeepAR.

This project is scoped as a research project with a focus on investigating potential AI solutions and not as a fully formed solution to the problem. A final ML solution would provide a pilot adequate time to perform evasive measures to mitigate the chances of a stall. Although the project dives into two algorithms and their use cases, the project does not have a fully vetted and ready algorithm to implement into a real world aircraft. The results of this project provide the basis for future algorithm development and implementation for a real world aircraft system.
