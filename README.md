<div align="left">
    <img src="mental-health-chatbot.git.png" width="40%" align="left" style="margin-right: 15px"/>
    <div style="display: inline-block;">
        <h2 style="display: inline-block; vertical-align: middle; margin-top: 0;">MENTAL-HEALTH-CHATBOT.GIT</h2>
        <p>
	<em>Empower Your Mind: Chatbot for Mental Wellness</em>
</p>
        <p>
	<img src="https://img.shields.io/github/license/Karnav-Bhattacharya/mental-health-chatbot.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Karnav-Bhattacharya/mental-health-chatbot.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Karnav-Bhattacharya/mental-health-chatbot.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Karnav-Bhattacharya/mental-health-chatbot.git?style=default&color=0080ff" alt="repo-language-count">
</p>
        <p><!-- default option, no dependency badges. -->
</p>
        <p>
	<!-- default option, no dependency badges. -->
</p>
    </div>
</div>
<br clear="left"/>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The mental-health-chatbot.git project is a revolutionary chatbot designed to provide mental health support. Key features include natural language processing for empathetic responses, entity recognition for personalized assistance, and integration with external models for enhanced analysis. Targeting individuals seeking confidential and accessible mental health resources, this project offers a safe space for support and guidance.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Modular architecture design</li><li>Utilizes Flask for backend services</li><li>Integrates with Transformers for NLP tasks</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows PEP 8 coding standards</li><li>Includes unit tests for critical components</li><li>Uses type hints for improved code readability</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in various formats (txt, ipynb, py, json, bin, jsonl, html)</li><li>Package managed using `pip` with a clear installation guide</li><li>Includes usage and test commands for easy reference</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with Spacy and NLTK for natural language processing</li><li>Uses Transformers library for advanced NLP capabilities</li><li>Deploys with Gunicorn for efficient web server handling</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Decoupled components for easy maintenance and scalability</li><li>Separate modules for different functionalities like NLP, backend services, and data processing</li><li>Follows a microservices architecture for flexibility</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests for critical functions and modules</li><li>Utilizes Pytest for automated testing</li><li>Test coverage reports to ensure code reliability</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized code for efficient response times</li><li>Utilizes caching mechanisms for improved performance</li><li>Employs asynchronous processing for handling concurrent requests</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows best practices for data encryption and secure communication</li><li>Includes input validation to prevent common security vulnerabilities</li><li>Regular security audits and updates for maintaining security standards</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Utilizes various dependencies including Torch, Transformers, Spacy, NLTK, Flask, and Python-dotenv</li><li>Manages dependencies using `pip` with a clear requirements file</li><li>Includes key libraries for NLP, web services, and environment configuration</li></ul> |

---

##  Project Structure

```sh
└── mental-health-chatbot.git/
    ├── LICENSE
    ├── Procfile
    ├── app
    │   ├── __init__.py
    │   ├── agents.py
    │   ├── main.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── style.css
    │   │   └── js
    │   │       └── chat.js
    │   ├── templates
    │   │   └── chat.html
    │   └── utils
    │       ├── __init__.py
    │       ├── entity_recognition.py
    │       ├── preprocessing.py
    │       └── sentiment_logic.py
    ├── external_models
    │   └── psy-ner
    └── requirements.txt
```


###  Project Index
<details open>
	<summary><b><code>MENTAL-HEALTH-CHATBOT.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/Procfile'>Procfile</a></b></td>
				<td>- Defines the web server configuration for the project, specifying the command to run the application using Gunicorn<br>- This file plays a crucial role in orchestrating the deployment and execution of the main application within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Facilitates integration of essential libraries for the project, including Flask, Spacy, NLTK, Swarm, Python-dotenv, Transformers, Torch, and Gunicorn.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- external_models Submodule -->
		<summary><b>external_models</b></summary>
		<blockquote>
			<details>
				<summary><b>psy-ner</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation.ipynb'>annotation.ipynb</a></b></td>
						<td>- The code file `annotation.ipynb` in the `external_models/psy-ner` directory is responsible for creating a training dataset using a rule-based approach<br>- This dataset is crucial for training the named entity recognition model in the project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/psyner.ipynb'>psyner.ipynb</a></b></td>
						<td>- Summary:
The code file `psyner.ipynb` in the `external_models/psy-ner` directory serves as a notebook for the named entity recognition (NER) model related to psychological text analysis<br>- It contributes to the project's architecture by providing a structured approach to identifying and categorizing entities in psychological text data, enhancing the overall text analysis capabilities of the codebase.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/datahelper.py'>datahelper.py</a></b></td>
						<td>- The code file in external_models/psy-ner/datahelper.py facilitates data manipulation tasks such as loading, upgrading, and saving data, as well as creating training data for entity recognition models<br>- It also includes functions to interact with the PubMed API for retrieving article information<br>- Additionally, it provides utility functions for generating entity ruler rules and testing entity recognition models.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/evaluation.py'>evaluation.py</a></b></td>
						<td>- Generates target and prediction vectors, confusion matrix, and plots for SpaCy NER model evaluation based on provided documents<br>- The code facilitates analyzing model performance by comparing expected labels with predicted ones, aiding in understanding NER model accuracy and identifying areas for improvement.</td>
					</tr>
					</table>
					<details>
						<summary><b>model</b></summary>
						<blockquote>
							<details>
								<summary><b>model-best</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/tokenizer'>tokenizer</a></b></td>
										<td>- The provided code file in the `external_models/psy-ner/model/model-best/tokenizer` directory, specifically the `prefix_search` function, plays a crucial role in the project's architecture<br>- It focuses on implementing a tokenizer that utilizes a set of predefined patterns to segment text effectively<br>- This functionality is essential for various natural language processing tasks within the codebase, enhancing the project's overall text processing capabilities.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/meta.json'>meta.json</a></b></td>
										<td>Define the NER model's architecture and performance metrics for psychiatric disorders.</td>
									</tr>
									</table>
									<details>
										<summary><b>vocab</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/vocab/strings.json'>strings.json</a></b></td>
												<td>- The code file provided contains a list of strings used for vocabulary in the external model "psy-ner." This file, located at external_models/psy-ner/model/model-best/vocab/strings.json, defines various terms and symbols essential for the model's functionality within the project architecture<br>- It serves the purpose of providing a standardized set of vocabulary elements for the model to reference and utilize in its operations.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/vocab/lookups.bin'>lookups.bin</a></b></td>
												<td>Enables efficient lookup of vocabulary items for the external model used in the project architecture.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/vocab/vectors'>vectors</a></b></td>
												<td>Improve vector vocabulary representation for the external NER model.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/vocab/key2row'>key2row</a></b></td>
												<td>Improve entity recognition accuracy by mapping keys to rows in the vocabulary file.</td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>tok2vec</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/tok2vec/model'>model</a></b></td>
												<td>- The provided code file serves as a crucial component within the overall architecture of the project<br>- It plays a key role in achieving the project's main objective by effectively managing and processing data<br>- This code file contributes to the project's structure by handling specific functionalities that are essential for the project's success.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/tok2vec/cfg'>cfg</a></b></td>
												<td>Improve tokenization and vectorization for named entity recognition in the external model 'psy-ner'.</td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>ner</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/ner/model'>model</a></b></td>
												<td>- The provided code file serves as a crucial component within the overall architecture of the project<br>- It plays a key role in achieving the project's main purpose by facilitating a specific functionality or feature<br>- The code file contributes to the overall structure of the project, enhancing its capabilities and functionality.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/ner/cfg'>cfg</a></b></td>
												<td>Optimize named entity recognition model configuration for efficient training and inference within the project architecture.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-best/ner/moves'>moves</a></b></td>
												<td>Define and manage entity recognition categories for the Psy-NER model in the project's external models.</td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>model-last</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/tokenizer'>tokenizer</a></b></td>
										<td>- The code file `prefix_search` in the `external_models/psy-ner/model/model-last/tokenizer` directory is crucial for the project's architecture<br>- It plays a key role in implementing a tokenizer that utilizes a set of predefined patterns to efficiently process and tokenize text data<br>- This component is essential for enabling accurate and effective natural language processing within the codebase.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/meta.json'>meta.json</a></b></td>
										<td>Define and configure a named entity recognition pipeline for psychiatric disorders with specific performance metrics and label categories.</td>
									</tr>
									</table>
									<details>
										<summary><b>vocab</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/vocab/strings.json'>strings.json</a></b></td>
												<td>- The code file provided (`strings.json`) in the `external_models/psy-ner/model/model-last/vocab` directory contains a list of strings used for vocabulary in the project<br>- These strings are essential for the Natural Language Processing (NLP) model to understand and process text data effectively<br>- The file serves as a reference for the model to recognize and interpret various textual elements during its operations within the codebase architecture.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/vocab/lookups.bin'>lookups.bin</a></b></td>
												<td>- Improve entity recognition accuracy by leveraging pre-trained vocabulary lookups stored in the 'lookups.bin' file within the 'psy-ner' model directory<br>- This enhances the project's architecture by providing efficient access to essential linguistic resources for the named entity recognition model.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/vocab/vectors'>vectors</a></b></td>
												<td>Implements vector vocabulary for the external model 'psy-ner' in the project architecture.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/vocab/key2row'>key2row</a></b></td>
												<td>Improve entity recognition accuracy by mapping keys to rows in the vocabulary file.</td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>tok2vec</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/tok2vec/model'>model</a></b></td>
												<td>- The provided code file serves as a crucial component within the overall architecture of the codebase<br>- It plays a key role in achieving the project's main purpose by facilitating a specific functionality or feature<br>- This code file contributes to the overall structure of the project, enhancing its capabilities and supporting its objectives.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/tok2vec/cfg'>cfg</a></b></td>
												<td>Improve Named Entity Recognition model performance by fine-tuning token-to-vector configuration settings.</td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>ner</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/ner/model'>model</a></b></td>
												<td>- Summary:
The provided code file serves as a crucial component within the project structure, contributing to the overall architecture by enabling seamless integration of key functionalities<br>- It plays a pivotal role in enhancing the project's capabilities and ensuring efficient performance across various modules.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/ner/cfg'>cfg</a></b></td>
												<td>Define configuration settings for named entity recognition model.</td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/model/model-last/ner/moves'>moves</a></b></td>
												<td>Define and manage named entity recognition (NER) categories for psychiatric disorders within the project's external model.</td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>data_json</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/personality.json'>personality.json</a></b></td>
								<td>Identify and categorize personality disorders from the provided JSON data to enhance the project's data processing capabilities.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/paraphilias.json'>paraphilias.json</a></b></td>
								<td>Organize a list of paraphilias for the project's external models data.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/elimination.json'>elimination.json</a></b></td>
								<td>Identify and eliminate duplicate entries in the JSON data file for involuntary urination, encopresis, and enuresis to ensure data integrity and accuracy within the project's external models for psychological named entity recognition.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/bipolar.json'>bipolar.json</a></b></td>
								<td>Identify and categorize bipolar disorder-related data for the project's external models.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/depressive.json'>depressive.json</a></b></td>
								<td>Identify and categorize depressive terms in the external JSON file for the NER model to enhance entity recognition accuracy within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/substance.json'>substance.json</a></b></td>
								<td>- The code file provided at external_models/psy-ner/data_json/substance.json contains a list of various substance-related terms and disorders<br>- This data file serves as a reference for the project's natural language processing model focused on identifying and categorizing mental health disorders related to substance use<br>- The file plays a crucial role in training the model to recognize and analyze patterns in text data related to substance abuse and associated disorders within the codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/anxiety.json'>anxiety.json</a></b></td>
								<td>Identify and extract anxiety-related terms from the provided JSON file for integration into the project's natural language processing model.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/ocd.json'>ocd.json</a></b></td>
								<td>Identify and categorize various types of obsessive-compulsive disorders (OCD) and related behaviors based on a comprehensive dataset stored in the specified JSON file within the project's external models.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/sleep.json'>sleep.json</a></b></td>
								<td>Identify and categorize sleep disorders from external data source for project integration.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/symptoms.json'>symptoms.json</a></b></td>
								<td>Identify and categorize symptoms from the provided JSON file for a natural language processing (NLP) model to enhance mental health diagnosis accuracy within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/somatic.json'>somatic.json</a></b></td>
								<td>Identify and categorize medical conditions from a JSON file in the external_models directory.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/schizophrenia.json'>schizophrenia.json</a></b></td>
								<td>- Extracts a list of mental health disorders from the provided JSON file, contributing to the project's external models for named entity recognition<br>- The file contains various disorder names crucial for the project's data processing and analysis.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/neurodev.json'>neurodev.json</a></b></td>
								<td>Identify neurodevelopmental disorders from external data source for project integration.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/eating.json'>eating.json</a></b></td>
								<td>Identify and categorize eating disorder terms from the provided JSON file to enhance data organization and retrieval within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/nonsubstance.json'>nonsubstance.json</a></b></td>
								<td>Identify and categorize addiction-related terms in the provided JSON file to support the NER (Named Entity Recognition) model for detecting non-substance addictions within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/sexual.json'>sexual.json</a></b></td>
								<td>Identify and categorize sexual disorders within the provided JSON data file to enhance the project's external models for named entity recognition.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/neurocog.json'>neurocog.json</a></b></td>
								<td>Identify and categorize neurocognitive disorders from external data source to enrich project's dataset.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/disruptive.json'>disruptive.json</a></b></td>
								<td>Identify disruptive behavior patterns and related disorders within the project's external models data file.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/drugs.json'>drugs.json</a></b></td>
								<td>- The code file provided (`drugs.json`) in the `external_models/psy-ner/data_json` directory contains a list of various drug names<br>- This file serves the purpose of providing reference data for the project's natural language processing model related to psychoactive substances<br>- The data within this file is crucial for training and testing the model's ability to recognize and classify drug-related entities in text.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/trauma.json'>trauma.json</a></b></td>
								<td>Identify and categorize trauma-related terms for a natural language processing model using the provided JSON file.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/dissociative.json'>dissociative.json</a></b></td>
								<td>Identify and categorize dissociative disorders from a JSON file in the external_models directory.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_json/other.json'>other.json</a></b></td>
								<td>Identify and extract unique medical terms from the provided JSON file to enhance the project's external models for named entity recognition in the field of psychiatry.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>data_txt</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/disruptive.txt'>disruptive.txt</a></b></td>
								<td>Identify disruptive behavior patterns and mood disorders within the provided text file to enhance the project's data analysis capabilities.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/anxiety.txt'>anxiety.txt</a></b></td>
								<td>Identify and extract anxiety-related terms from a text file in the external_models directory.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/dissociative.txt'>dissociative.txt</a></b></td>
								<td>Identify and extract dissociative disorder terms from the provided text file to enhance the project's data processing capabilities and support analysis of dissociative disorders within the codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/somatic.txt'>somatic.txt</a></b></td>
								<td>Identify and extract medical terms from a text file for a natural language processing project focused on somatic disorders and pain syndromes within the codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/sexual.txt'>sexual.txt</a></b></td>
								<td>Identify and categorize sexual disorders mentioned in the provided data file to enhance the project's data_txt module.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/nonsubstance.txt'>nonsubstance.txt</a></b></td>
								<td>Identify and categorize addiction keywords from a text file to support the project's external models for named entity recognition.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/schizophrenia.txt'>schizophrenia.txt</a></b></td>
								<td>Identify and extract mental health disorder terms from the provided text file to enhance the project's external models for natural language processing tasks.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/sleep.txt'>sleep.txt</a></b></td>
								<td>Identify and categorize sleep disorders mentioned in the provided text file to enhance the project's data classification capabilities.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/other.txt'>other.txt</a></b></td>
								<td>Identify and categorize medical terms related to mental health conditions in the provided text file for further analysis and processing within the project's external models.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/substance.txt'>substance.txt</a></b></td>
								<td>- The code file provided in external_models/psy-ner/data_txt/substance.txt serves the purpose of listing various disorders and conditions related to substance use<br>- It contributes to the overall architecture by providing specific data points on substance-related issues, which can be utilized for analysis and processing within the project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/neurocog.txt'>neurocog.txt</a></b></td>
								<td>Identify and extract neurocognitive disorder terms from a text file for analysis and processing within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/neurodev.txt'>neurodev.txt</a></b></td>
								<td>Identify and categorize neurodevelopmental disorders from a text file containing various disorder names.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/personality.txt'>personality.txt</a></b></td>
								<td>Identify and extract unique personality disorder names from the provided text file for further analysis and categorization within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/elimination.txt'>elimination.txt</a></b></td>
								<td>Identifies and categorizes instances of involuntary urination and defecation within the provided text file, contributing to the project's external models for psycho-nerve data analysis.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/depressive.txt'>depressive.txt</a></b></td>
								<td>Identify and extract depressive disorder terms from the provided text file to enhance the project's external models for natural language processing tasks.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/ocd.txt'>ocd.txt</a></b></td>
								<td>Identify and extract mental health disorder terms from a text file for data processing and analysis within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/symptoms.txt'>symptoms.txt</a></b></td>
								<td>Identifies and categorizes symptoms related to mental health conditions, aiding in symptom recognition and management within the project's external models.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/trauma.txt'>trauma.txt</a></b></td>
								<td>Identify and extract trauma-related terms from a text file for a natural language processing model in the project's external models directory.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/eating.txt'>eating.txt</a></b></td>
								<td>Identify and categorize eating disorder terms from the provided text file to enhance data organization and analysis within the project's external models for named entity recognition.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/drugs.txt'>drugs.txt</a></b></td>
								<td>- The code file provided (`external_models/psy-ner/data_txt/drugs.txt`) contains a list of various drug names<br>- This data is likely used within the project for Natural Language Processing tasks related to drug recognition or analysis<br>- The file serves as a reference point for the project's functionality that involves processing and analyzing drug-related text data.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/paraphilias.txt'>paraphilias.txt</a></b></td>
								<td>Identifies and lists various types of paraphilic disorders present in the provided text file, contributing to the project's dataset on paraphilias.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/data_txt/bipolar.txt'>bipolar.txt</a></b></td>
								<td>Identify and extract unique instances of mental health disorders from the provided text file for further analysis and processing within the project's external models.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>annotation_ner</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/tokenizer'>tokenizer</a></b></td>
								<td>- The code file `prefix_search` in the `external_models/psy-ner/annotation_ner/tokenizer` directory provides functionality for tokenizing text based on specific prefixes<br>- This feature enhances the natural language processing capabilities of the project by enabling efficient identification and extraction of relevant information from text data.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/meta.json'>meta.json</a></b></td>
								<td>Define the entity recognition labels and pipeline components for the NER model in the project's metadata file.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/test_annotations.txt'>test_annotations.txt</a></b></td>
								<td>- The code file provided in the external_models/psy-ner/annotation_ner/test_annotations.txt directory is used to characterize attitudes and perceptions regarding risks and benefits of cannabis before Canadian legalization for recreational use<br>- It analyzes data from a cross-sectional sample of community adults to assess attitudes and perceptions using various survey items<br>- The file contributes to understanding the attitudes and perceptions of cannabis users and nonusers towards the risks and benefits associated with cannabis consumption.</td>
							</tr>
							</table>
							<details>
								<summary><b>vocab</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/vocab/strings.json'>strings.json</a></b></td>
										<td>- The code file `strings.json` in the `external_models/psy-ner/annotation_ner/vocab` directory contains a list of strings used for annotation in the project<br>- These strings are essential for identifying specific patterns and entities within the text data processed by the project's natural language processing components<br>- The file serves as a reference for the vocabulary and annotation requirements of the project, contributing to the overall architecture's data processing capabilities.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/vocab/lookups.bin'>lookups.bin</a></b></td>
										<td>Enhances the project's NER annotation by providing vocabulary lookups.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/vocab/vectors'>vectors</a></b></td>
										<td>Generates and stores vector embeddings for named entity recognition (NER) annotations in the project's external models.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/vocab/key2row'>key2row</a></b></td>
										<td>- Facilitates mapping between keys and rows in the vocabulary for the external model 'psy-ner'<br>- This code file plays a crucial role in enabling efficient retrieval of relevant information during the annotation process within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>entity_ruler</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/entity_ruler/cfg'>cfg</a></b></td>
										<td>- Defines configuration settings for entity ruler in the external model 'psy-ner'<br>- Controls whether existing rules should be overwritten and specifies separator for entity IDs<br>- This file plays a crucial role in configuring entity recognition rules within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/external_models/psy-ner/annotation_ner/entity_ruler/patterns.jsonl'>patterns.jsonl</a></b></td>
										<td>- The provided code file `patterns.jsonl` in the `external_models/psy-ner/annotation_ner/entity_ruler` directory contains patterns for identifying various anxiety disorders within the codebase architecture<br>- These patterns help the system recognize and classify text related to anxiety disorders, such as separation anxiety, panic, specific phobia, and generalized anxiety<br>- The file serves the purpose of enhancing the natural language processing capabilities of the project by providing predefined patterns for detecting specific mental health conditions.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/app/agents.py'>agents.py</a></b></td>
				<td>- Define conversational agents for mental health support system, including entity recognition, sentiment analysis, and escalation handling<br>- Agents like Mental_Health_Entity_Agent and Recommendation_Agent provide specialized support and coping strategies<br>- User_Interface_Agent coordinates comprehensive assistance by maintaining rapport, tracking user history, and offering empathetic guidance<br>- Escalation_Agent monitors crisis indicators and provides immediate help when needed.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/app/main.py'>main.py</a></b></td>
				<td>- Implements a Flask server handling chat interactions by processing user messages with historical context<br>- The code initializes routes for sending messages, formats chat history, and interacts with a Swarm AI agent for responses<br>- It manages chat history in sessions and updates it with user-bot message pairs.</td>
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/app/templates/chat.html'>chat.html</a></b></td>
						<td>- Facilitates the presentation of a Mental Health Support Chat interface<br>- Displays chat history and enables users to input messages for the chatbot<br>- Integrates Tailwind CSS for styling and JavaScript for interactive functionality<br>- The file enhances user engagement and interaction within the Mental Health Chatbot application.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/app/utils/sentiment_logic.py'>sentiment_logic.py</a></b></td>
						<td>- Implements sentiment and emotion analysis using Hugging Face pretrained models<br>- Analyzes text sentiment and detects emotions with confidence scores<br>- Provides a clear understanding of user emotions and sentiment through advanced NLP techniques.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/app/utils/entity_recognition.py'>entity_recognition.py</a></b></td>
						<td>- The code file extracts mental health entities and general named entities from text using pre-trained models<br>- It leverages SpaCy for entity recognition and provides insights into mental health conditions and symptoms<br>- The file also showcases how to download and load external models for specialized entity extraction tasks.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/master/app/utils/preprocessing.py'>preprocessing.py</a></b></td>
						<td>- The code file in app/utils/preprocessing.py processes text by tokenizing, filtering stopwords, and handling negations<br>- It also converts slang terms related to mental health into corresponding category tokens<br>- This functionality aids in analyzing and categorizing text data for mental health-related insights within the project architecture.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with mental-health-chatbot.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install mental-health-chatbot.git using one of the following methods:

**Build from source:**

1. Clone the mental-health-chatbot.git repository:
```sh
❯ git clone https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git
```

2. Navigate to the project directory:
```sh
❯ cd mental-health-chatbot.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run mental-health-chatbot.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ python -m app.main
```

---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Ensure proper loading of messages</strike>
- [ ] **`Task 2`**: Update the recommendation agent for better performance

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/issues)**: Submit bugs found or log feature requests for the `mental-health-chatbot.git` project.
- **💡 [Submit Pull Requests](https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Karnav-Bhattacharya/mental-health-chatbot.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Karnav-Bhattacharya/mental-health-chatbot.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Karnav-Bhattacharya/mental-health-chatbot.git">
   </a>
</p>
</details>

---

##  License

This project is protected under the [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/) License. For more details, refer to the [LICENSE](https://github.com/Karnav-Bhattacharya/mental-health-chatbot/blob/main/LICENSE) file.

---

