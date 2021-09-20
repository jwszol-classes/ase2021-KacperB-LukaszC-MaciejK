# <center>**Projekt ASEiED**</center>
 ## Zadanie projektowe
 Dokonaj analizy danych zawierających informacje na temat poruszających się taksówek w Nowym Jorku (yellow and green taxi). Zbiór danych zawiera następujące informacje (pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts).

 * Rok 2020 / Maj
 * Rok 2019 / Maj

 b) Skoreluj informacje dotyczące typu płatności a ilości przewożonych pasażerów 

 ## Wykorzystane technologie

* Amazon EMR
* Amazon EMR Notebooks
* Apache Spark
* Pyspark

Klaster komputerowy został utworzony z wykorzystaniem platformy **Amazon EMR**. Został na nim uruchomiony kernel **Pyspark**, który posłużył do wykonywania kodu zawartego w aplikacji **Jupyter Notebook**. Taka konfiguracja umożliwiła uruchomienie **aplikacji Sparkowej** na klastrze wykorzustując do jej programowania **API pythonowe**.  

 ## Konfiguracja klastra

 W celu stworzenia klastra komputerowego umożliwiającego uruchomienie kernela Pyspark należy postępować zgodnie z poniższymi krokami:
1. W konsoli aws wyszukujemy **EMR** i przechodzimy do zaznaczonego serwisu
   ![Model](./zdjecia/emr.png)
2. Klikamy create cluster
    ![Model](./zdjecia/create.png)
3. Naciskamy go to advanced options
   ![Model](./zdjecia/advanced.png)
4. Zaznaczamy odpowiednie ustawienia software'u
   ![Model](./zdjecia/apps.png)
5. Przechodzimy do ustawień hardwaru i wybieramy interesującą nas konfiguracje klastra:
   ![Model](./zdjecia/nodes.png)
6. Przechodzimy do ogólnych ustawień i wybieramy nazwe klastra
   ![Model](./zdjecia/name.png)
7. Przechodzimy do kolejnej sekcji i klikamy create cluster.
   ![Model](./zdjecia/createcluster.png)

Reszta ustawień może pozostać domyślna. Bardziej zaawansowane sposoby konfiguracji zostały opisane w [1], [2].

W celu połączenia klastra z **notebookiem EMR** przechodzimy do sekcji Notebooks i tworzymy nowy notebook
![Model](./zdjecia/notebooks.png)

W oknie tworzenia nowego notebooka wybieramy utworzony przez nas klaster i klikamy create notebook 
![Model](./zdjecia/createnote.png)

W zakładce **notebooks** powinniśmy znaleźc stworzony notebook ze statusem **ready**
![Model](./zdjecia/notebook_created.png)

Otwieramy stworzony przez nas notebook i uruchamiamy go w JupyterLab
![Model](./zdjecia/notebook_open.png)

Zostajemy przekierowani na stronę z projektem w jupyter lab. Wybieramy kernel **PySpark**
![Model](./zdjecia/notebook_open.png)

Stworzone przez nas środowisko umożliwia na uruchomienie kodu napisanego w języku **python** rozszerzonego o biblioteke **pyspark**. 
![Model](./zdjecia/kernel.png) 


[1]: <https://towardsdatascience.com/how-to-set-up-a-cost-effective-aws-emr-cluster-and-jupyter-notebooks-for-sparksql-552360ffd4bc>
[2]: <https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-considerations.html>