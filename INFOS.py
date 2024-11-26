INFOS = {
        "Planifier" : """Dans le modèle SCOR, le processus Plan englobe toutes les activités stratégiques visant à équilibrer 
                        la demande et les ressources dans la chaîne d'approvisionnement. Il consiste à prévoir la demande, 
                        planifier les ressources, optimiser les coûts et coordonner les opérations pour atteindre les objectifs 
                        de performance.\n Ce processus sert de base pour les autres étapes du modèle SCOR (Source, Make, Deliver, Return) 
                        et inclut également l'élaboration de plans alternatifs pour gérer les risques. Il joue un rôle central dans 
                        l’alignement des fonctions clés et l'amélioration globale de l'efficacité et de la réactivité de la chaîne 
                        d'approvisionnement.""",
        "sP1" : """Le développement et l’établissement de plans d’action sur des périodes de temps spécifiées qui représentent 
        une allocation projetée des ressources de la chaîne d’approvisionnement, afin de répondre aux besoins
        de la chaîne d’approvisionnement tout en tenant compte des contraintes de disponibilité des ressources à long terme.""",
        "sP1.1" : "Identifier, Prioriser et Agréger les Besoins de la Chaîne d'Approvisionnement",
        "sP1.2" : "Identifier, Prioriser et Agréger les Ressources de la Chaîne d'Approvisionnement",
        "sP1.3" : "Équilibrer les Ressources de la Chaîne d'Approvisionnement avec les Exigences de la Chaîne",
        "sP1.4" : "Élaborer et Communiquer les Plans de la Chaîne d'Approvisionnement",
        
        "sP2" : """Le développement et l’établissement de plans d’action sur des périodes de temps spécifiées
        qui représentent une allocation projetée des ressources matérielles afin de répondre aux exigences 
        de la chaîne d’approvisionnement""",
        "sP2.1" : "Identifier, prioriser et regrouper les exigences des produits.",
        "sP2.2" : "Identifier, évaluer et regrouper les ressources des produits",
        "sP2.3" : "Équilibrer les ressources produit avec les exigences produit.",
        "sP2.4" :"Établir des plans d'approvisionnement",
        
        "sP3" : """Le développement et l'établissement de plans d'action sur des périodes de temps spécifiées
        qui représentent une affectation projetée des ressources de production pour répondre
        aux exigences de production""",
        "sP3.1" : "Établir des plans d'approvisionnement",
        "sP3.2" : ": Identifier, évaluer et agréger les ressources de production",
        "sP3.3" : ": Équilibrer les ressources de production avec les exigences de production",
        "sP3.4" :"Établir des plans de production",
       
        "sP4" : """Développement et établissement de plans d'action sur des périodes de temps définies représentant une allocation projetée des ressources de livraison pour répondre aux exigences de livraison.""",
        "sP4.1" : "Identifier, prioriser et agréger les exigences de livraison",
        "sP4.2" : "Identifier, évaluer et agréger les ressources de livraison",
        "sP4.3" : "Équilibrer les ressources et capacités de livraison avec les exigences de livraison",
        "sP4.4" :"Établir des plans de livraison",
        
        "sP5" : """Un processus stratégique ou tactique visant à établir et ajuster des plans d'action ou des
        tâches sur des périodes de temps définies, représentant une allocation projetée des ressources et
        des actifs nécessaires à la gestion des retours afin de répondre aux besoins anticipés et non anticipés
        en matière de retours.""",
        "sP5.1" : "Évaluer et agréger les besoins en retours",
        "sP5.2" : "Identifier, évaluer et agréger les ressources de retour",
        "sP5.3" : "Équilibrer les ressources de retour avec les besoins en retours",
        "sP5.4" :"Établir et communiquer les plans de retours",
        
        "Approvisionner": """Les processus d'approvisionnement (Source) décrivent la commande 
        (ou la planification des livraisons) et la réception des biens et services.
        Le processus d'approvisionnement englobe l'émission de bons de commande ou
        la planification des livraisons, la réception, la validation et le stockage des biens,
        ainsi que l'acceptation de la facture du fournisseur. À l'exception des biens ou services
        Sourcing Engineer-to-Order, tous les processus d'identification, de qualification et de négociation
        des contrats avec les fournisseurs ne sont pas décrits par les éléments du processus Source.
        Les noms de niveau trois sont inclus ici, mais les définitions se trouvent uniquement dans le cadre SCOR.",
        "sS1": "Le processus d'approvisionnement, de réception et de transfert d'articles de matières premières,
        de sous-ensembles, de produits finis et/ou de services basé sur des besoins en demande agrégée.
        L'objectif de l'approvisionnement pour stockage (Source-to-Stock) est de maintenir un niveau prédéterminé
        de stock pour ces matériaux, sous-ensembles ou produits. Aucune référence ou commande client n'est échangée
        avec le fournisseur, associée au produit ou enregistrée dans le système de gestion d'entrepôt (WMS) ou dans
        le système ERP pour les produits Source-to-Stock. Exemples de noms alternatifs ou connexes pour 
        Source-to-Stock :Inventaire de réapprovisionnement, pièces goutte à goutte, kanban, andon, stock en vrac ou générique.""",
        "sS1.1": "Planifier les livraisons de produits.",
        "sS1.2": "Réceptionner les produits.",
        "sS1.3": "Vérifier le produit.",
        "sS1.4": "Transférer le produit.",
        "sS1.5": "Autoriser le paiement du fournisseur.",
        
        "sS2": """Les processus d'approvisionnement pour un produit sur commande consistent à commander et à recevoir
        des produits ou des matériaux qui sont commandés (et peuvent être configurés) uniquement lorsque cela est 
        requis par une commande client spécifique. L'objectif de l'approvisionnement sur commande (Source-to-Order)
        est de maintenir un inventaire commandé (et/ou configuré) spécifiquement pour des commandes clients uniquement.
        Le produit est commandé, reçu et identifié en stock en utilisant la référence de la commande client
        (l'inventaire désigné est généralement identifiable tout au long du processus d'approvisionnement,
        par la référence à la commande client attachée au produit ou à son emballage, ainsi que dans
        le système de gestion d'entrepôt ou ERP).Exemples de noms alternatifs ou connexes pour
        Source-to-Order :Commande spéciale (secteur de la vente au détail), séquencement de ligne (industries), 
        achat sur commande, kitting (assemblage de composants pour la fabrication).""",
        "sS2.1": "Planifier les livraisons de produits.",
        "sS2.2": "Réceptionner le produit.",
        "sS2.3": "Vérifier le produit.",
        "sS2.4": "Transférer le produit.",
        "sS2.5": "Autoriser le paiement du fournisseur.",
       
        "sS3": """Les processus d'identification et de sélection des sources d'approvisionnement, de négociation,
        de validation, de planification, de commande et de réception des pièces, des sous-ensembles ou des produits
        spécialisés ou services qui sont conçus, commandés et/ou fabriqués en fonction des exigences ou des spécifications
        d'une commande client spécifique""",
        "sS3.1": "Identifier les sources d'approvisionnement.",
        "sS3.2": "Sélectionner le fournisseur final et négocier.",
        "sS3.3": "Planifier les livraisons de produits.",
        "sS3.4": "Réceptionner le produit.",
        "sS3.5": "Vérifier le produit.",
        "sS3.6": "Transférer le produit.",
        "sS3.7": "Autoriser le paiement du fournisseur.",
        
        "Fabriquer": """Les processus de fabrication (Make) décrivent les activités associées
        à la transformation des matériaux ou à la création de contenu pour les services.
        Le terme transformation des matériaux est utilisé plutôt que production ou fabrication,
        car le processus de fabrication (Make) englobe tous les types de transformations de matériaux
        : Assemblage, Traitement chimique, Maintenance, Réparation, Rénovation, Recyclage, Remise à neuf,
        Remanufacturation et d'autres noms courants pour les processus de transformation des matériaux.
        En règle générale, ces processus sont reconnus par le fait qu'un ou plusieurs numéros d'article entrent
        dans le processus, et un ou plusieurs numéros d'article différents en sortent.Les noms de niveau trois sont
        inclus ici, mais les définitions se trouvent uniquement dans le cadre SCOR.",
        "sM1": "Le processus d'ajout de valeur à un produit livrable, par la fabrication ou la création d'un produit
        ou d'un livrable ; ou dans les industries de services, par la création de livrables de service.
        Les produits fabriqués sur stock sont destinés à être expédiés à partir de produits finis ou
        prêts à l'emploi basés sur un catalogue de produits/services prédéfini. Ils peuvent être fabriqués
        avant la réception d'une commande client et sont généralement produits selon un planning prévu,
        en fonction d'une prévision des ventes. Aucune référence client, détail de commande ou spécification
        n'est attachée aux commandes de production ou de service, ni attachée au produit, ni marquée sur le produit,
        ni enregistrée dans le système de gestion de la production ou ERP pour les produits fabriqués sur stock.
        Les produits ou services configurables ne peuvent pas être livrés via le processus de livraison de produits stockés,
        car les produits configurables nécessitent une référence client ou des détails de commande client.""",
        "sM1.1": "Planifier les activités à valeur ajoutée",
        "sM1.2": "Emettre le matériel/ Identifier les ressources",
        "sM1.3": "Produire et tester",
        "sM1.4": "Emballer",
        "sM1.5": "Mettre en scène le produit/la ressource",
        "sM1.6": "Libérer le produit/la ressource pour la livraison",
        "sM1.7": "Elimination des déchets",
        
        "sM2": """Le processus d'ajout de valeur à un produit ou à un livrable, que ce soit par la fabrication
        ou la création d'un produit, ou dans les industries de services, par la création de livrables
        de service pour une commande client spécifique. Les produits et services sont complétés, 
        fabriqués ou configurés uniquement en réponse à une commande client. La référence de la commande client
        est attachée à la commande de production ou de service, marquée sur le produit ou le livrable une
        fois le processus de fabrication terminé, et utilisée lors du transfert du produit vers la phase de livraison.
        Le produit est identifiable tout au long du processus à valeur ajoutée, car il est fabriqué pour une commande
        client spécifique.Exemples de noms alternatifs ou connexes pour Fabrication sur commande :Build-to-Order (BTO),
        Assemble-to-Order (ATO), Configure-to-Order (CTO), et report de la production (postponement).""",
        "sM2.1": "Planifier les activités de production",
        "sM2.2": "Émettre le produit sourcé / en cours de production",
        "sM2.3": "Produire et tester",
        "sM2.4": "Emballer",
        "sM2.5": "Mettre en scène le produit fini",
        "sM2.6": "Libérer le produit pour la livraison",
        "sM2.7": "Elimination des déchets",
        
        "sM3": """Le processus d'ajout de valeur à un produit ou à un livrable,
        soit par la fabrication ou la création d'un produit, soit dans les industries de services,
        par la création de livrables de service, où l'objet de la livraison n'est pas entièrement
        défini au début du processus.Il s'agit du processus de développement, de conception, 
        de validation et, finalement, de l'utilisation d'un processus à valeur ajoutée pour produire
        des produits ou des services basés sur les exigences d'un client spécifique. En général,
        l'Ingénierie sur commande (Engineer-to-Order) nécessite que les instructions de travail soient
        définies ou affinées, et que les instructions de routage des matériaux soient ajoutées ou modifiées.
        Exemple de nom alternatif ou connexe pour l'Ingénierie sur commande :Design-to-Order (DTO).""",
        "sM3.1": "Finaliser l'ingénierie de production",
        "sM3.2": "Planifier les activités de production",
        "sM3.3": "Emettre le produit sourcé/ en cours de production",
        "sM3.4": "Produire et tester",
        "sM3.5": "Emballer",
        "sM3.6": "Mettre en scène le produit fini",
        "sM3.7": "Libérer le produit pour la livraison",
        "sM3.8":"Elimination des déchets",
        
        "Livrer": """Le processus de livraison décrit les activités associées à la création,
        à la maintenance et à l'exécution des commandes des clients. Le processus de livraison
        comprend la validation de la réception et la création des commandes clients, la planification
        des commandes, la livraison, le prélèvement, l'emballage et l'expédition et la facturation au client.
        Le processus de livraison et de vente au détail sD4 offre une vue simplifiée des processus d'approvisionnement
        et de livraison exploités dans une opération de make-to-stock-only dans la vente au détailLes noms de niveau
        trois sont inclus ici mais les définitions ne se trouvent que dans le cadre Scor",
        "sD1": "le processus de livraison de produits provenant de commandes clients agrégées ou fabriqués
        sur la base de commandes clients, commandes projetées / demande et paramètres de réapprovisionnement des stocks.
        L'intention de livrer un produit en stock est d'avoir le produit disponible lorsqu'une commande client arrive
        (pour empêcher le client de chercher ailleurs). Pour les industries de services, il s'agit de services prédéfinis
        et prêts à l'emploi (par exemple une formation standard). Les produits ou services « configurables » ne peuvent pas
        être livrés via le processus de livraison de produits en stock, car les produits configurables nécessitent
        une référence client ou des détails de commande client.""",
        "sD1.1": "Processus de demande et devis.",
        "sD1.2": "Recevoir, saisir et valider la commande.",
        "sD1.3": "Réserver l'inventaire et déterminer la date de livraison.",
        "sD1.4": "Consolider les commandes.",
        "sD1.5": "Construire des charges.",
        "sD1.6": "Expéditions par route.",
        "sD1.7": "Sélectionner les transporteurs et taux d'expédition.",
        "sD1.8": "Recevoir le produit de la source ou fabriquer.",
        "sD1.9": "Prélever le produit.",
        "sD1.10": "Emballer le produit.",
        "sD1.11": "Charger le véhicule et générer les documents d'expédition.",
        "sD1.12": "Expédier le produit.",
        "sD1.13": "Recevoir et vérifier les produits par le client.",
        "sD1.14": "Installer le produit.",
        "sD1.15": "Facturer.",
       
        "sD2": """Processus de livraison d'un produit/service acheté, configuré,
        fabriqué et/ou assemblé à partir de matières premières, de pièces,
        d'ingrédients ou de sous-ensembles standards en réponse à une commande client ferme.
        Une référence à la commande client est échangée avec le processus d'approvisionnemen
        t ou de valeur ajoutée et attachée ou marquée sur le produit/service. Les produits en stock
        sont identifiables par la commande client grâce à l'étiquetage et à la gestion des données d'inventaire.
        Les exemples incluent l'attribution d'un numéro de série ou d'un numéro de lot à une commande client
        avant la fabrication ou l'approvisionnement, les processus qui génèrent une nomenclature pour le processus
        de fabrication associé (par exemple, la configuration à la commande et l'assemblage à la commande) et le
        processus de « commande spéciale » dans le commerce de détail.""",
        "sD2.1": "Processus de demande et devis.",
        "sD2.2": "Recevoir, configurer, saisir et valider la commande.",
        "sD2.3": "Réserver l'inventaire et déterminer la date de livraison.",
        "sD2.4": "Consolider les commandes.",
        "sD2.5": "Construire des charges.",
        "sD2.6": "Expéditions par route.",
        "sD2.7": "Sélectionner les transporteurs et taux d'expédition.",
        "sD2.8": "Recevoir le produit de la source ou fabriquer.",
        "sD2.9": "Prélever le produit.",
        "sD2.10": "Emballer le produit.",
        "sD2.11": "Charger le véhicule et générer les documents d'expédition.",
        "sD2.12": "Expédier le produit.",
        "sD2.13": "Recevoir et vérifier les produits par le client.",
        "sD2.14": "Installer le produit",
        "sD2.15": "Facturer",
        
        "sD3": """Processus de livraison d'un produit/service acheté, configuré,
        fabriqué et/ou assemblé à partir de matières premières, de pièces, d'ingrédients
        ou de sous-ensembles standards en réponse à une commande client ferme. Une référence
        à la commande client est échangée avec le processus d'approvisionnement ou de valeur ajoutée
        et attachée ou marquée sur le produit/service. Les produits en stock sont identifiables
        par la commande client grâce à l'étiquetage et à la gestion des données d'inventaire.
        Les exemples incluent l'attribution d'un numéro de série ou d'un numéro de lot à une commande client
        avant la fabrication ou l'approvisionnement, les processus qui génèrent une nomenclature pour
        le processus de fabrication associé (par exemple, la configuration à la commande et l'assemblage à la commande)
        et le processus de « commande spéciale » dans le commerce de détail.""",
        "sD3.1": "Obtenir et répondre à RFP/RFQ",
        "sD3.2": "Négocier et recevoir le contrat",
        "sD3.3": "Saisissez la commande, engagez les ressources et lancez le programme",
        "sD3.4": "Programmer l'installation",
        "sD3.5": "Construire des charges.",
        "sD3.6": "Expéditions par route.",
        "sD3.7": "Sélectionner les transporteurs et taux d'expédition.",
        "sD3.8": "Recevoir le produit de la source ou fabriquer.",
        "sD3.9": "Prélever le produit.",
        "sD3.10": "Emballer le produit.",
        "sD3.11": "Charger le véhicule et générer les documents d'expédition.",
        "sD3.12": "Expédier le produit.",
        "sD3.13": "Recevoir et vérifier les produits par le client.",
        "sD3.14": "Installer le produit",
        "sD3.15": "Facturer",
        
        "sD4": """La livraison de produits au détail est le processus utilisé pour acquérir,
        commercialiser et vendre des produits finis dans un magasin de détail.
        Un magasin de détail est un emplacement physique qui vend des produits (et des services)
        directement au consommateur en utilisant un processus de point de vente (manuel ou automatisé)
        pour percevoir le paiement. Le marchandisage au niveau d'un magasin consiste à stocker
        et à réapprovisionner des produits dans des emplacements de stockage désignés pour générer
        des ventes dans un magasin de détail.""",
        "sD4.1": "Générer un calendrier de stockage",
        "sD4.2": "Recevoir le produit en magasion",
        "sD4.3": "Prélever le produit dans l'arrière boutique",
        "sD4.4": "Etagère de stockage",
        "sD4.5": "Remplir le panier",
        "sD4.6": "Caisse",
        "sD4.7": "Livrer et/ou installer",
        
        "Retour": """Les processus de retour décrivent les activités associées au flux inverse des marchandises.
        Le processus de retour comprend l'identification du besoin de retour, la prise de décision quant
        à l'élimination, la planification du retour ainsi que l'expédition et la réception des marchandises retournées.
        Les processus de réparation, de recyclage, de remise à neuf et de reconditionnement ne sont pas décrits décrits
        à l'aide d'éléments de processus de retour. Voir fabrication.Les noms de niveau trois sont inclus ici,
        mais les définitions ne se trouvent que dans le cadre SCOR.",
        "sSR1": "La détermination du retour et de la disposition des produits défectueux tels que 
        définis par les réclamations de garantie, le rappel des produits, les produits non conformes et/ou
        d'autres politiques similaires, y compris le remplacement approprié. Le retour d'un produit
        défectueux prend en charge tout type de produit non conforme aux spécifications, y compris
        la non-conformité de la commande telle qu'une livraison tardive ou autrement incorrecte) ;
        les règles commerciales de l'entreprise déterminent la définition de « défectueux ».
        La disposition physique du produit peut ne pas faire partie du processus de retour.""",
        "sSR1.1": "Identifier l'état du produit défectueux",
        "sSR1.2": "Disposition produit défectueux",
        "sSR1.3": "Demander une autorisation de retour de produit défectueux",
        "sSR1.4": "Planifier l'expédition des produits défectueux",
        "sSR1.5": "Retourner le produit défectueux",
        
        "sDR1": """La détermination du retour et de la disposition des produits défectueux tels
        que définis par les réclamations de garantie, le rappel des produits, les produits non
        conformes et/ou d'autres politiques similaires, y compris le remplacement approprié.
        Le retour d'un produit défectueux prend en charge tout type de produit non conforme
        aux spécifications (y compris la non-conformité de la commande telle qu'une livraison
        tardive ou autrement incorrecte) ; les règles commerciales de l'entreprise déterminent
        la définition de « défectueux ». La disposition physique du produit peut ne pas faire
        partie du processus de retour.""",
        "sDR1.1": "Autoriser le retour effectif du produit",
        "sDR1.2": "Programmer une réception pour un retour défectueux",
        "sDR1.3": "Recevoir un produit défectueux (vérification incluse)",
        "sDR1.4": "Transférer le produit défectueux",

        "sSR2": """Le retour de produits ou d'actifs de l'entreprise en vue de leur réception,
        de leur réparation ou de leur mise à niveau, tel que défini par les plans de maintenance
        ou l'apparition ou l'anticipation d'un risque de défaillance. En général, les actifs de l'entreprise
        gérés par un processus MRO doivent être remis en état et remis en service. Le processus de
        retour ne représente pas les activités réelles de maintenance, de réparation ou de révision ;
        celles-ci sont généralement représentées par des processus de fabrication. La disposition physique
        des produits peut ne pas faire partie du processus de retour.""",
        "sSR2.1": "Identifier l'état des produits MRO",
        "sSR2.2": "Disposition des produits MRO",
        "sSR2.3": "Demander une autorisation de retour de produit MRO",
        "sSR2.4": "Planifier l'expédition du produit MRO",
        "sSR2.5": "Retourner le produit MRO",

        "sDR2": """La réception de produits ou d'actifs de l'entreprise destinés à la maintenance,
        à la réparation et à la révision (MRO) dans le but de les recevoir, de les réparer ou
        de les mettre à niveau, comme défini par les plans de maintenance ou l'apparition
        ou l'anticipation d'un risque de défaillance. En général, les actifs de l'entreprise
        gérés par un processus MRO doivent être remis en état et remis en service.
        Le processus de retour ne représente pas les activités réelles de maintenance,
        de réparation ou de révision ; celles-ci sont généralement représentées par
        des processus de fabrication. La disposition physique des produits peut ne pas
        faire partie du processus de retour.""",
        "sDR2.1": "Autoriser le retour du produit MRO",
        "sDR2.2": "Planifier la réception du retour MRO",
        "sDR2.3": "Recevoir les produits MRO",
        "sDR2.4": "Transférer le produit MRO",

        "sSR3": """Le retour d'un inventaire excédentaire ou vieillissant
        ou de produits obsolètes tel que défini par les termes et conditions
        d'un contrat client/fournisseur. Le but des retours de produits excédentaires
        est de réaffecter l'inventaire à un emplacement ou une organisation qui peut
        vendre le produit considéré comme excédentaire dans l'emplacement actuel.
        La disposition physique des produits peut ne pas faire partie du processus de retour.",
        "sSR3.1": "Identifier l'état des produits excédentaires""",
        "sSR3.2": "Élimination des produits excédentaires",
        "sSR3.3": "Demander l'autorisation de retour des produits excédentaires",
        "sSR3.4": "Planifier l'expédition des produits excédentaires",
        "sSR3.5": "Retourner les produits excédentaires",

        "sDR3": """La réception d'un inventaire excédentaire ou vieillissant
        ou de produits obsolètes, tel que défini par les termes et conditions
        d'un contrat client/fournisseur. Le but des retours de produits excédentaires
        est de réaffecter l'inventaire à un emplacement ou une organisation qui peut
        vendre le produit considéré comme excédentaire dans l'emplacement actuel.
        La disposition physique des produits peut ne pas faire partie du processus de retour. """,
        "sDR3.1": "Autoriser le retour du produit excédentaire",
        "sDR3.2": "Planifier la réception du retour du produit excédentaire",
        "sDR3.3": "Recevoir le produit excédentaire",
        "sDR3.4": "Transférer le produit excédentaire",
        
         "Autoriser / Activer": """Les processus associés à l'établissement,
         à la maintenance et au suivi des informations, des relations,
         des ressources, des actifs, des règles commerciales,
         de la conformité et des contrats nécessaires au fonctionnement de la chaîne d'approvisionnement
         ainsi qu'au suivi et à la gestion des performances globales de la chaîne d'approvisionnement.
         Les processus d'activation fournissent des informations et des orientations essentielles pour
         soutenir la réalisation et la gouvernance des processus de planification et d'exécution
         des chaînes d'approvisionnement. Les processus d'activation interagissent et gèrent l'alignement
         avec les processus d'autres domaines (par exemple : processus financiers,
         processus RH (ressources humaines), processus I(C)T (information, communication et technologie),
         processus de gestion des installations, processus de gestion des produits et du portefeuille,
         processus de conception des produits et des processus et processus de vente et de support).
         Les noms de niveau trois sont inclus ici, mais les définitions ne se trouvent que dans le cadre SCOR.""",
        "sE1": """Processus d'établissement, de documentation, de communication et de publication
        des règles commerciales de la chaîne d'approvisionnement. Une règle commerciale est une déclaration
        ou un paramètre qui définit ou restreint certains aspects de l'entreprise et est généralement utilisé
        dans la prise de décision. Les règles commerciales sont destinées à influencer les résultats
        de l'exploitation de la chaîne d'approvisionnement. Les règles commerciales peuvent s'appliquer
        aux personnes, aux processus, au comportement de l'entreprise et aux systèmes informatiques
        d'une organisation, et sont mises en place pour aider l'organisation à atteindre ses objectifs
        tout en maintenant la conformité aux politiques et lois internes et externes.Un exemple de règle
        commerciale peut stipuler « aucun retour accepté sans autorisation de retour ».
        Les types de règles commerciales de la chaîne d'approvisionnement comprennent :
        • Objectifs de performance
        • Règles pour assurer ou faire respecter la conformité aux réglementations et aux politiques (par exemple, ITAR)
        • Règles de planification telles que la fréquence, l'horizon et le niveau des plans, la planification des nomenclaturespolitiques (par exemple ITAR)
        • Règles de planification telles que la fréquence, l'horizon et le niveau des plans, nomenclatures de planification
        • Règles d'approvisionnement telles que les fournisseurs approuvés, les fournisseurs sur liste noire
        • Nomenclatures de fabrication, règles de maintenance des équipements
        • Règles de service client et de segmentation de la clientèle telles que le délai d'exécution des commandes,
        les méthodes et niveaux de stockage des stocks, les combinaisons origine/destination autorisées
        • Règles logistiques telles que les itinéraires et les modes, les fournisseurs de services de transport,
        d'entreposage et de 3PL approuvés
        • Politiques de retour de produits, règles d'élimination des produits défectueux, règles de remboursement/remplacement
        • Règles de collaboration pour aligner la prise de décision dans les organisations
        • Remarque : sE1 Manage Les règles métier ne développent généralement pas de politiques, elles traduisent
        les politiques en règles métier appliquées aux processus de la chaîne d'approvisionnement.""",
        "sE1.1": "Collecter les exigences des règles métier",
        "sE1.2": "Interpréter les exigences des règles métier",
        "sE1.3": "Documenter la règle métier",
        "sE1.4": "Communiquer la règle métier",
        "sE1.5": "Publier/diffuser la règle métier",
        "sE1.6": "Retirer la règle métier",
       
        "sE2": """Processus de définition des objectifs de performance pour les mesures
        de la chaîne d'approvisionnement qui s'alignent sur la stratégie et les objectifs
        globaux de l'entreprise, et de reporting des performances, d'identification des écarts de performance,
        d'analyse des causes profondes et de développement et de lancement d'actions correctives pour combler
        les écarts de performance. Ce processus décrit tous les niveaux et versions de gestion des performances
        de la chaîne d'approvisionnement. Exemples :
        • Comptage des cycles d'inventaire
        • Optimisation des stocks projets
        • Réduction du temps de cycle de commande efforts
        • Production et processus programmes d'amélioration de la qualité
        • Performance des fournisseurs évaluations
        • Processus et pratique évaluations de maturitéRemarque : il est courant que les organisations
        disposent de plusieurs versions de ce processus, dans différentes parties de l'organisation.
        Aux niveaux 3 et 4, ces processus peuvent différer considérablement selon la dépend de manière
        significative des objectifs de chacun de ces processus de gestion des performances""",
        "sE2.1": "Initier le reporting",
        "sE2.2": "Analyser les rapports",
        "sE2.3": "Trouver les causes profondes",
        "sE2.4": "Prioriser les causes profondes",
        "sE2.5": "Élaborer des actions correctives",
        "sE2.6": "Approuver et lancer",
       
        "sE3": """Processus de collecte, de maintenance et de publication des données
        et informations nécessaires à la planification, à l'exploitation,
        à la mesure et à la gestion de la chaîne d'approvisionnement.
        Exemples de catégories d'éléments de données :
        • Données de base : données fondamentales sur les clients, les fournisseurs,
        les matières premières, les nomenclatures, les recettes, les produits,
        les personnes, les processus et les actifs nécessaires au fonctionnement
        de la chaîne d'approvisionnement
        • Données transactionnelles : données associées à l'achat,
        à la réception, aux mouvements de matériaux, aux opérations à valeur ajoutée, au stockage,
        à la préparation, à l'emballage, à l'expédition et à la livraison de matériaux et de produits
        • Données de collaboration : données des partenaires de la chaîne d'approvisionnement qui fournissent
        la visibilité de la chaîne d'approvisionnement inter-organisationnelle nécessaire pour
        planifier et exécuter la chaîne d'approvisionnement de manière intégrée de bout en bout
        • Métadonnées : données qui décrivent et ajoutent des informations sur d'autres données
        • Données de performance : données métriques et données d'entrée brutes associées nécessaires au calcul""",
        "sE3.1": "Recevoir une demande de maintenance""",
        "sE3.2": "Déterminer/définir la portée des travaux",
        "sE3.3": "Maintenir le contenu/code",
        "sE3.4": "Maintenir l'accès",
        "sE3.5": "Publier des informations",
        "sE3.6": "Vérifier les informations",
       
        "sE4": """Processus de développement, de gouvernance et de maintenance
        d'une organisation de personnel permanent, temporaire et externalisé,
        doté des qualifications adéquates, en soutien aux objectifs commerciaux
        et à la chaîne d'approvisionnement. Cela comprend l'identification
        des compétences requises et disponibles dans l'organisation,
        la détermination des lacunes en termes de compétences et de niveaux de compétence,
        l'identification des besoins de formation, des lacunes en matière de ressources
        et des ressources excédentaires. Remarque : il s'agit d'un processus de planification
        visant à garantir que le personnel (capacité) est disponible aux bons niveaux.
        La formation, l'embauche et le redéploiement proprement dits ne font pas partie
        de ce processus, car il s'agit de processus RH.""",
        "sE4.1": "Identifier les compétences/ressources requises",
        "sE4.2": "Identifier les compétences/ressources disponibles",
        "sE4.3": "Associer les compétences/ressources",
        "sE4.4": "Déterminer l'embauche/le redéploiement",
        "sE4.5": "Déterminer la formation/l'éducation",
        "sE4.6": "Approuver, prioriser et lancer",
       
        "sE5": """Processus de planification, de maintenance et de disposition 
        des actifs de la chaîne d'approvisionnement développés pour
        l'exécution de la chaîne d'approvisionnement. Cela comprend l'installation,
        la réparation, la modification, l'étalonnage et d'autres activités nécessaires
        pour soutenir l'exécution de la chaîne d'approvisionnement.Discussion :
        il s'agit davantage d'un processus de planification visant à garantir que les actifs (capacité)
        sont disponibles aux bons niveaux au bon moment. Les processus de maintenance, etc.
        réels sont décrits à l'aide de processus SCOR standard. Par exemple 
        : le processus d'exécution de la maintenance de routine sur un camion est décrit
        à l'aide des processus de retour MRO et/ou de fabrication.""",
        "sE5.1": "Planifier les activités de gestion des actifs",
        "sE5.2": "Mettre l'actif hors ligne",
        "sE5.3": "Inspecter et dépanner",
        "sE5.4": "Installer et configurer",
        "sE5.5": "Nettoyer, entretenir et réparer",
        "sE5.6": "Mettre hors service et éliminer",
        "sE5.7": "Inspecter l'entretien",
       
        "sE6": """La gestion et la communication des accords contractuels et non contractuels
        à l'appui des objectifs commerciaux et des objectifs de la chaîne d'approvisionnement.
        Cela comprend tous les accords liés aux opérations de la chaîne d'approvisionnement, notamment :
        l'acquisition de matériel et de services, les pratiques et les niveaux de stockage des stocks,
        les objectifs de performance, la planification et la prise de décision, la logistique et la livraison,
        ainsi que l'échange et la visibilité des données.
        Remarques : cela couvre l'ancien sES.10 et des parties de sES.6, sEM.6, sED.6, sER.6.
        L'identification et la sélection des fournisseurs et les négociations contractuelles résident
        dans les processus DCOR (et partiellement dans sS3). La recherche de clients et la clôture des contrats clients
        résident dans les processus CCOR.""",
        "sE6.1": """Planifier les activités de gestion des actifs""",
        "sE6.2": "Mettre l'actif hors ligne",
        "sE6.3": "Inspecter et dépanner",
        "sE6.4": "Installer et configurer",
        "sE6.5": "Nettoyer, entretenir et réparer",
        "sE6.6": "Mettre hors service et éliminer",
        "sE6.7": "Inspecter l'entretien",
        
        "sE7": """Processus de définition et de gestion de l'empreinte géographique 
        et des activités de la chaîne d'approvisionnement. Il définit l'emplacement
        des installations et les affections de ressources, réseaux de distribution,
        fournisseurs, clients ; matériaux, produits, capacités et/ou aptitudes à ces emplacements.""",
        "sE7.1": "Sélectionner la portée et l'organisation",
        "sE7.2": "Rassembler les données et les commentaires",
        "sE7.3": "Élaborer des scénarios",
        "sE7.4": "Modéliser/simuler des scénarios",
        "sE7.5": "Impact du projet",
        "sE7.6": "Sélectionner et approuverr",
        "sE7.7": "Élaborer un programme de changement",
        "sE7.8": "Lancer un programme de changement",
        
        "sE8": """Processus d'identification, de collecte, d'évaluation
        et d'intégration des exigences de conformité réglementaire dans les processus,
        politiques et règles commerciales standard de la chaîne d'approvisionnement.
        Ce processus comprend également la gestion de la conformité volontaire aux normes
        et certifications.La conformité réglementaire est le terme généralement utilisé
        pour décrire les politiques et processus mis en place par les organisations pour
        garantir qu'elles se conforment aux lois, règles et réglementations mises en place par
        des organismes externes (gouvernementaux) qui contrôlent l'activité dans une juridiction donnée.
        Souvent, les organisations choisissent d'aller au-delà de la conformité réglementaire pour
        respecter les normes de conformité volontaire et/ou de rechercher des certifications volontaires
        pour des raisons stratégiques. Les exemples de conformité volontaire aux normes
        et certifications incluent : les normes ISO et les certifications facultatives
        telles que Rain Forest Alliance Certified, Sustainable Forestry Initiative, etc.
        Un élément clé de la conformité réglementaire/volontaire La conformité consiste
        à établir des politiques, des règles commerciales et des processus pour garantir
        le respect des exigences législatives et réglementaires. Cela implique de s'assurer
        que le personnel est informé et prend des mesures pour se conformer aux lois,
        réglementations et normes en vigueur, ainsi qu'à la conservation des données
        ou des dossiers utilisés pour la validation de la conformité. Les exemples de conformité
        réglementaire incluent : C-TPAT, matières dangereuses, importation/exportation, main-d'œuvre,
        licences, taxes. Remarque : il s'agit d'exemples, SCOR ne fournit pas (ne tente pas de fournir)
        une liste complète.""",
        "sE8.1": "Surveiller les entités réglementaires",
        "sE8.2": "Évaluer les publications réglementaires",
        "sE8.3": "Identifier les lacunes réglementaires",
        "sE8.4": "Définir la remédiation",
        "sE8.5": "Vérifier/Obtenir une licence",
        "sE8.6": "Publier la remédiation",
        
        "sE9": """"Processus d'identification et d'évaluation des perturbations potentielles (risques)
        dans la chaîne d'approvisionnement et élaboration d'un plan visant à atténuer ces menaces
        pour le fonctionnement de la chaîne d'approvisionnement. Les risques liés à la chaîne d'approvisionnement
        comprennent :\n
        • Perturbations de la demande – par exemple, des clients qui cessent leurs activités\n
        • Perturbations de l'approvisionnement - par exemple, faillite de fournisseurs, problèmes
        de qualité/performance des fournisseurs
        • Perturbations environnementales – par exemple, intempéries,
        inondations, tremblements de terre
        • Perturbations financières – par exemple disponibilité du crédit, investisseurs
        • Fraude, vol et mauvaise gestion – absence de risque atténuation
        • Perturbation du travail – p. ex. grèves des salariés, manque de personnel qualifié
        • Terrorisme et cybercriminalité attaquesLes stratégies d’atténuation des risques comprennent
        l’évitement du risque, la réduction de l’impact ou de la probabilité du risque,
        le transfert du risque à une autre partie et l’acceptation d’une partie du risque. Risque.
        Exemples de modifications apportées au réseau, aux processus et aux ressources
        de la chaîne d'approvisionnement : assurance, relocalisation, approvisionnement double/triple,
        externalisation, internalisation, délocalisation, relocalisation, sécurité, refonte
        de la chaîne d'approvisionnement, refonte des processus, modifications des règles commerciales,
        renégociation des contrats. sE9 Gérer les risques de la chaîne d'approvisionnement est étroitement
        aligné sur la section 5 de la norme ISO 31000. ISO31000 est une norme de gestion des risques générique
        pour l'ensemble de l'entreprise, sE9 - Gérer les risques de la chaîne d'approvisionnement
        est l'adaptation pour la gestion des risques de la chaîne d'approvisionnement.
        Remarque : la section 5.6 de l'ISO 31000, Suivi et examen, est représentée dans SCOR
        par sE2 Gérer les performances de la chaîne d'approvisionnement.""",
        "sE9.1": "Établir le contexte",
        "sE9.2": "Identifier les événements à risque",
        "sE9.3": "Quantifier les risques",
        "sE9.4": "Évaluer les risquesr",
        "sE9.5": "Stratégie de gestion des risques",
        "sE9.6": "Surveiller",
        
        
        "sE10": """Le cycle d'approvisionnement est le processus cyclique des étapes clés
        de l'acquisition de biens ou de services.Les concepts de cette section ont été 
        élaborés en conjonction avec les normes d'approvisionnement définies par
        le Chartered Institute of Procurement & Supply (CIPS). Pour plus d'informations
        sur les pratiques d'approvisionnement et d'approvisionnement reconnues à l'échelle mondiale,
        veuillez consulter le site Web du CIPS à l'adresse www.cips.org""",
        "sE10.1": "Élaborer une stratégie et un plans",
        "sE10.2": "Pré-approvisionnement / Test de marché et engagement du marché",
        "sE10.3": "Élaborer la documentation, PPQ / Spécifications détaillées",
        "sE10.4": "Sélection des fournisseurs pour participer à l'ITT / RFQ / Négociation",
        "sE10.5": "Émettre l'ITT / RFQ",
        "sE10.6": "Évaluation et validation des offres",
        "sE10.7": "Attribution et mise en œuvre du contrat",
        
        "sE11": """Processus de définition, de déploiement et de gestion de l'habilitation 
        technologique impliquée dans la planification, l'exécution et la gestion des performances
        de la chaîne d'approvisionnement. La portée de l'habilitation technologique
        dans la chaîne d'approvisionnement va bien au-delà des systèmes ERP et MRP de base pour inclure :
        • Systèmes de planification
        • Portails fournisseurs
        • Outils de sourcing etplates-formes
        • Exécution de la fabrication systèmes (MES)
        • Outils de modélisation et d’analyse de la chaîne d’approvisionnement
        • Capteurs et solutions Internet des objets (IoT)
        • Solutions d'automatisation des processus et des activités
        • Outils et plateformes de visibilité et de collaboration sur la chaîne d'approvisionnement
        • Outils et plateformes de surveillance et de gestion des risques de la chaîne d'approvisionnement
        • Mesures et rapports outils
        • Détection de la demande technologies (par exemple, réseaux sociaux) (suivi et analyse)Discussion 
        : De nombreuses organisations disposent de processus à l'échelle de l'entreprise pour gérer la technologie.
        Ce processus n'a pas pour but de dupliquer ou de remplacer ces processus d'entreprise,
        mais vise à renforcer la nécessité d'une attention et d'une participation
        ciblées de l'organisation de la chaîne d'approvisionnement dans la définition
        des exigences et des choix technologiques pour la chaîne d'approvisionnement.
        Il n'inclut pas les activités de gestion informatique standard pour tester
        et mettre en œuvre de nouvelles solutions technologiques.""",
        "sE11.1": "Définir les exigences technologiques de la chaîne d'approvisionnement",
        "sE11.2": "Identifier les alternatives de solutions technologiques",
        "sE11.3": "Définir/mettre à jour la feuille de route technologique de la chaîne d'approvisionnement",
        "s11.4": "Sélectionner la solution technologiquer",
        "sE11.5": "Définir et déployer la solution technologique",
        "sE11.6": "Maintenir et améliorer la solution technologique",
        "sE11.7": "Retirer la solution technologique",
####################################################################################################
        "Fiabilité" : """  L'attribut fiabilité aborde la capacité à effectuer les taches comme recquis. La fiabilité se concentre sur la présivibilité du résultat d'un processus """,
            """RL1.1""": """Définition : Le pourcentage de commandes respectant la performance de livraison avec une documentation complète et précise et sans dommage de livraison.
Les composants incluent tous les articles et quantités à temps selon la définition du client de la ponctualité, ainsi que la documentation - bordereaux d'expédition, lettres de transport, factures, etc.
Le dictionnaire APICS définit la commande parfaite comme une commande dans laquelle les "sept R" sont satisfaits : le bon produit, la bonne quantité, la bonne condition, le bon endroit, le bon moment, le bon client et le bon coût. Le modèle SCOR aborde les "sept R" à travers une seule métrique stratégique appelée Satisfaction de Commande Parfaite (POF) qui regroupe le bon produit et la bonne quantité en une seule métrique de niveau 2. 2 métriques appelées % de Commandes Livrées en Intégralité, le bon moment et le bon emplacement (et le bon client implicite) sont regroupées en une métrique de niveau 2 appelée Performance de Livraison à la Date d'Engagement du Client, la bonne condition est mesurée dans la métrique de niveau 2 Condition Parfaite et le bon coût est mesuré avec l'attribut stratégique global Coût.

Calcul [Total des Commandes Parfaites] / [Total des Commandes] x 100%
Remarque : une commande est parfaite si les articles individuels qui composent cette commande sont tous parfaits.
Le calcul de la satisfaction de commande parfaite est basé sur la performance de chaque composant de niveau 2 de la ligne de commande à calculer. (Produit et quantité, date et heure et client, documentation et état). Pour qu'une ligne de commande soit parfaite, tous les composants individuels doivent être parfaits.
""",
            """RL2.1""": """Définition : Pourcentage des commandes pour lesquelles tous les articles sont reçus par le client en quantités engagées. Le nombre de commandes reçues par le client dans les quantités engagées divisé par le nombre total de commandes.
Calcul : [Nombre total de commandes livrées en totalité] / [Nombre total de commandes livrées] x 100%. Une commande est considérée comme livrée "en totalité" si : • Tous les articles commandés sont les articles effectivement fournis, et aucun article supplémentaire n'est fourni • Toutes les quantités reçues par le client correspondent aux quantités commandées (dans les limites de tolérance convenues d'un commun accord).
""",
            """RL2.2""": """Définition : Le pourcentage de commandes qui sont remplies à la date initialement convenue avec le client. Calcul : [Nombre total de commandes livrées à la date d'engagement initiale] / [Nombre total de commandes livrées] x 100%. Une commande est considérée comme livrée à la date d'engagement initiale du client si :
* La commande est reçue à temps comme défini par le client • La livraison est effectuée au bon emplacement et à l'entité du client.

""",
            "RL2.3": """
Définition : Pourcentage des commandes avec une documentation précise et à temps soutenant la commande: y compris les bordereaux d'expédition, les connaissements, les factures, etc. Calcul : [Nombre total de commandes livrées avec une documentation précise] / [Nombre total de commandes livrées] x 100%. Une commande est considérée comme ayant une documentation précise lorsque les éléments suivants sont acceptés par le client :
La documentation soutenant la commande comprend : • Documentation d'expédition : • Bordereaux de livraison (Clients) • Connaissement (Transporteurs) • Documentation / formulaires gouvernementaux ou douaniers • Paiement
Documentation : • Facture • Accord-cadre contractuel • Documentation de conformité
• Fiches de données de sécurité des matériaux
• Autres documents requis • Certification de qualité. Toute la documentation doit être complète, correcte et facilement disponible lorsque et comme attendu par le client, le gouvernement et les autres entités réglementaires de la chaîne d'approvisionnement.

""",
            "RL2.4": """Définition : Pourcentage des commandes livrées en parfait état, conformes aux spécifications, avec la configuration correcte, installées sans défaut (le cas échéant) et acceptées par le client. Calcul :
[Nombre de commandes livrées en parfait état] / [Nombre de commandes livrées] x 100%. Une commande est considérée comme livrée en parfait état si tous les articles répondent aux critères suivants : • Non endommagé
• Conforme aux spécifications et avec la configuration correcte (as applicable) • Installé sans défaut (le cas échéant) et accepté par le client
• Non retourné pour réparation ou remplacement (pendant la période de garantie).

""",
            "RL3.X": "Les mesures de niveau 3 servent de diagnostics pour les mesures de niveau 2.",
        "Réactivité": """L'attribut réactivité décrit la vitesse à laquelle les taches sont exécutées""",
            "RS.1.1" : """Le délai de cycle moyen réellement atteint pour exécuter les commandes des clients. Pour chaque commande individuelle, ce délai de cycle commence à la réception de la commande et se termine avec l'acceptation de la commande par le client.
[Somme de délais de cycle réels pour toutes les commandes livrées] /[nombre total de commandes livrés]en jours 
""",
             "RS.2.1": """Le temps moyen associé aux processus source (processus : S1, S2, S3)
Délai de cycle source= (Identifier les sources d’approvisionnement) + (Sélectionner le fournisseur et négocier) + (Planifier les livraisons de produits) + (Recevoir le produit) + (Vérifier le produit) + (Transférer le produit) + (Autoriser le paiement du fournisseur)
""",
            "RS.2.2": """Le temps moyen associé aux processus de fabrication :
Délai de cycle de fabrication = (Finaliser le cycle de l’ingénierie de production) + (Planifier les activités de production) + (Emettre les matériaux / produits) + (Produire et tester) + (Emballer) + (Mettre en stock le produit fini) + (Libérer le produit fini pour la livraison)""" ,
            "RS.2.3": """délai de cycle de livraison :
Délai de cycle de retour=max [(Ressources et déterminer la date de livraison) + (Consolider les commandes + Planifier l’installation) + (Construire les charges) + (Acheminer les envois) + (Sélectionner les transporteurs et  évaluer les envois),(Recevoir le produit du cycle de fabrication / approvisionnement)] + Sélectionner le produit + Emballer le produit + Charger le véhicule et générer la documentation d’expédition + Expédier le produit + (Recevoir et vérifier le produit) + Installer le produit""",
            "RS.2.4": """Le délai de cycle de livraison au détail pourrait être calculé comme la somme des étapes mentionnées ci-dessus :
Délai de cycle de livraison au détail=Prise de commande + Traitement de la commande + Emballage + Transport/expédition + Livraison + Réception et acceptation du produit""",
            "RS.2.5":""" Le délai de cycle de retour fait référence au temps moyen nécessaire pour traiter un produit retourné, depuis le moment où le besoin de retour est identifié jusqu'à ce que le produit retourné soit vérifié, réintégré en stock ou correctement traité. Cela englobe toutes les étapes du processus de gestion des retours dans un magasin de détail.
Délai de cycle de retour = Identifier le besoin de retour + Coordonner et planifier le retour + Temps de transit du retour + Temps de réception du produit retourné + Vérifier et transférer le produit retourné""",
            "RS.3.X": """
Les métriques de niveau 3 servent de diagnostics pour les métriques de niveau 2""",
        "Agilité":""" L'attribut Agilité décrit la capacité à répondre aux influences externes ; la capacité et la rapidité de changement. Les influences externes comprennent : des augmentations ou des diminutions imprévisibles de la demande, des fournisseurs ou partenaires faisant faillite, des catastrophes naturelles, des actes de terrorisme (cyber) ou de guerre, la disponibilité des ressources financières (l'économie), des problèmes de main-d'œuvre. Les indicateurs de performance clés SCOR incluent la Flexibilité, l'Adaptabilité et la Valeur en Risque. L'agilité est un attribut axé sur le client.""",
            "AG.1.1": """Il s'agit de l'augmentation maximale soutenable en pourcentage de la quantité livrée qui peut être atteinte en 30 jours. Remarques : Les 30 jours sont un chiffre arbitraire fourni à des fins de référence. Pour certaines industries et certaines organisations, 30 jours peuvent être dans certains cas inatteignables ou, dans d'autres cas, trop conservateurs. Remarque : Les métriques de composants (Adaptabilité de l'approvisionnement à la hausse, Adaptabilité de la fabrication à la hausse, etc.) peuvent être améliorées en parallèle et, par conséquent, ce calcul nécessite que le résultat soit la moindre augmentation de quantité soutenable en 30 jours. Le nouveau niveau d'exploitation doit être atteint sans une augmentation significative du coût par unité.
Calcul : L'adaptabilité de la chaîne d'approvisionnement est la quantité la moins élevée soutenable lorsqu'on considère les composants Source, Make, Deliver et Return
""",
            "AG.2.2": """il s'agit de l'augmentation maximale soutenable en pourcentage de la production qui peut être réalisée en 30 jours, en supposant qu'il n'y a pas de contraintes liées aux matières premières""",
            "AG.2.3": """Il s'agit de l'augmentation maximale soutenable en pourcentage des quantités livrées qui peut être réalisée en 30 jours, en supposant que la disponibilité des produits finis n'est pas contrainte.""",
            "AG.2.4": """Cela concerne l'augmentation maximale soutenable en pourcentage des retours qui peuvent être traités dans un délai de 30 jours, en supposant qu'il n'y a pas de contraintes dans la capacité à traiter ces retours.""",
            "AG.2.5": """Il s'agit de l'augmentation maximale soutenable en pourcentage des retours de produits finis des clients qui peut être réalisée en 30 jours
""",
            "AG.1.2": """Il s'agit de la réduction des quantités commandées soutenable 30 jours avant la livraison, sans pénalité liée aux stocks ou aux coûts. Remarque : Les 30 jours sont un chiffre arbitraire fourni à des fins de référence. Pour certaines industries et certaines organisations, 30 jours peuvent être inatteignables dans certains cas ou trop conservateurs dans d'autres.
Calcul : Adaptabilité à la baisse de l'approvisionnement + Adaptabilité à la baisse de la fabrication + Adaptabilité à la baisse de la livraison.
L'adaptabilité de la chaîne d'approvisionnement à la baisse est la réduction minimale soutenable lorsqu'on considère les composants Source, Make, Deliver et Return.
""",
            "AG.2.6": """Il s'agit de la réduction de la quantité de matières premières soutenable 30 jours avant la livraison, sans pénalité liée aux stocks ou aux coûts""",
            "AG.2.7": """Il s'agit de la réduction de la production soutenable 30 jours avant la livraison, sans pénalité liée aux stocks ou aux coûts.""",
            "AG.2.8": """Il s'agit de la réduction des quantités livrées soutenable 30 jours avant la livraison, sans pénalité liée aux stocks ou aux coûts.""",
            "AG.1.4": """La gestion des risques dans les organisations réside traditionnellement dans la fonction finance, en raison de son focus inhérent sur l'impact financier sur l'organisation. Cependant, la plupart des organisations n'évaluent pas le risque de la chaîne d'approvisionnement séparément. Ces dernières années, la gestion des risques de la chaîne d'approvisionnement (SCRM) est devenue un domaine d'intérêt pour les responsables financiers en charge de la gestion des risques d'entreprise. Par conséquent, il est nécessaire d'établir un langage commun pour monétiser le risque de la chaîne d'approvisionnement. La valeur en risque (VaR) est une métrique de risque populaire largement utilisée par l'industrie financière pour comprendre l'exposition au risque d'un portefeuille de trading basé sur la volatilité historique.
Calcul simple de la VaR:
VaR=Probabilité de l’événement de risque (P) x Impact monétiséˊ de l’événement de risque (I).
""",
            "AG.2.9": """Il s'agit de l'évaluation numérique du risque pour un fournisseur, un client ou un produit. Cette évaluation est normalisée et utilisée à des fins de comparaison.""",
            "AG.2.10": """VIl s'agit de la somme des probabilités des événements de risque multiplié par l'impact monétaire de ces événements dans toutes les activités de planification. Un événement de risque peut ici être défini comme un écart par rapport à la valeur métrique attendue pour le processus.""",
            "AG.2.11": """Il s'agit de la somme des probabilités des événements de risque multiplié par l'impact monétaire de ces événements dans toutes les activités d'approvisionnement. Un événement de risque peut ici être défini comme un écart par rapport à la valeur métrique attendue pour le processus.""",
            "AG.2.12": """Il s'agit de la somme des probabilités des événements de risque multiplié par l'impact monétaire de ces événements dans toutes les activités de fabrication. Un événement de risque peut ici être défini comme un écart par rapport à la valeur métrique attendue pour le processus.""",
            "AG.2.13": """Il s'agit de la somme des probabilités des événements de risque multiplié par l'impact monétaire de ces événements dans toutes les activités de livraison. Un événement de risque peut ici être défini comme un écart par rapport à la valeur métrique attendue pour le processus""",
            "AG.2.14": """Il s'agit de la somme des probabilités des événements de risque multiplié par l'impact monétaire de ces événements dans toutes les activités de retour. Un événement de risque peut ici être défini comme un écart par rapport à la valeur métrique attendue pour le processus.""",
            "AG.2.15": """Le Temps de Récupération (TTR) correspond au temps total nécessaire pour qu'un point du réseau retrouve un fonctionnement complet après une perturbation. Cela inclut le temps de récupération total, en combinant les informations de TTR des fournisseurs avec les données propres à l'organisation pour identifier l'exposition au risque de chaque site du réseau.""",
        "Coût": """L'attribut Cout décrit le cout d'exploitation du processus de la chaine logistique""",
            "CO.1.1": """Définition : La somme des coûts associés aux
Processus SCOR de niveau 2 pour planifier, approvisionner, livrer et retourner. Remarque : le coût des matières premières et les coûts de fabrication sont généralement comptabilisés dans le coût des marchandises vendues. Il est reconnu qu'il est probable qu'il y ait un chevauchement/une redondance entre les coûts de gestion de la chaîne logistique et le coût des marchandises vendues. CTGCA = Coût de planification + Coût d'approvisionnement + Coût de fabrication + Coût de livraison + Coût de retour + Coûts d'atténuation.
""",
            "CO.2.1": """Définition : La somme des coûts associés au Plan.
Calcul : Coût de Planification = Somme du Coût de
Planification (Plan + Source + Fabrication +
Livraison + Retour).
""",
            "CO.2.2": """Définition : La somme des coûts associés à
Source. Calcul : Coût d'approvisionnement = Somme
Des coûts pour (Gestion des fournisseurs +
Gestion de l'acquisition de matériel)
•Gestion des fournisseurs = planification des matériaux + planification du personnel d'approvisionnement + négociation et qualification des fournisseurs + etc. •Gestion de l'acquisition de matériel = appels d'offres et devis + commandes + réception + inspection des matériaux entrants + stockage des matériaux + autorisation de paiement + règles et exigences d'approvisionnement + fret et droits de douane entrants + etc.
""",
            "CO.2.3": """Définition : La somme des coûts associés à la fabrication. Remarque : - Le coût des matières premières et les coûts de fabrication sont généralement inclus dans le COGS. Il est reconnu qu'il y a probablement un chevauchement/une redondance entre les coûts de gestion de la chaîne d'approvisionnement et le COGS.
Calcul : Coût de fabrication = Somme des coûts directs de matériel, de main-d'œuvre directe et de coûts directs non matériels liés au produit (équipement) et des coûts indirects liés au produit (NE fait PAS partie du CO.1.2 Coût des marchandises vendues.)
""",
            "CO.2.4": """Définition : La somme des coûts associés à la Livraison et/ou à l'Installation. Calcul :
Calcul : Coût de livraison = Somme des coûts
de (Gestion des commandes + Gestion des clients) •Gestion des commandes de vente = demandes de renseignements et devis + saisie et maintenance des commandes + gestion des canaux + exécution des commandes + distribution + transport + fret sortant et droits + installation + facturation / comptabilité client + lancement de nouveaux produits / phase d'introduction + etc. •Gestion de la clientèle = financement + service après-vente + gestion des litiges + réparations sur site + technologies de facilitation + etc.
""",
            "CO.2.5": """Définition : Coût de retour d'un produit défectueux - La somme des coûts associés au retour d'un produit défectueux au fournisseur.
(Processus : sSR1, sDR1) Coût de retour des produits excédentaires - La somme des coûts associés au retour des produits excédentaires au fournisseur. (Processus : sSR3, sDR3)
Coût de retour du produit MRO - La somme des coûts associés au retour du produit MRO au fournisseur.
""",
           "CO.2.6": """Définition : Le coût d'atténuation ($) est une mesure diagnostique pour CO.11 : Coût de gestion de la chaîne logistique (total). La somme des coûts associés à la gestion des risques non systémiques qui découlent de variations de causes spéciales au sein de la chaîne logistique (définies comme des variations qui ne sont pas prévisibles ; ont une cause attribuable ; et dont le modèle d'occurrence n'est pas inhérent au comportement du système ; sont plutôt non naturelles) (voir la section Discussion dans SCOR pour plus d'informations).""",
            "CO.1.2": """Définition : Le coût associé à l'achat de matières premières et à la production de biens finis.
Ce coût comprend les coûts directs (main-d'œuvre, matériaux) et les coûts indirects. (Frais généraux).
Remarque : Le coût des matières premières et les coûts de fabrication sont généralement inclus dans le COGS. Il est reconnu qu'il y a probablement un chevauchement/une redondance entre les coûts de gestion de la chaîne d'approvisionnement et le COGS.
Calcul : Coût des marchandises vendues (CMV) =
Coût de fabrication. COGS = coûts directs des matériaux + coûts directs de la main-d'œuvre + coûts indirects liés à la fabrication du produit.
""",
            "CO.2.7": """Coût direct dépensé pour les matériaux de production.
""",
            "CO.2.8": """Les coûts indirects engagés dans la production de manière indirecte.""",
            "CO.2.9": """Coût indirect lié à la production""",
            "CO.3.X": """"Les mesures de niveau 3 servent de diagnostic pour les mesures de niveau 2.""",             
        "Gestion d'actifs" : """L'attribut Gestion d'actifs décrit la capacité à utilisier efficacement les actifs""",
            "AM.1.1": """Le cycle de trésorerie représente le temps nécessaire pour qu’un investissement effectué revienne à l’entreprise après avoir été dépensé, par exemple, pour l’achat de matières premières. Pour les services, il s’agit du temps entre le paiement des ressources utilisées pour fournir un service et le moment où l’entreprise reçoit le paiement de ces services de la part du client.
Formule :
Cycle de Trésorerie = [Jours de Stock Disponible] + [Délai de Recouvrement des Créances Clients] - [Délai de Paiement Fournisseurs], exprimé en jours.
""",
            "AM.2.1": """Le délai de recouvrement des créances clients mesure la durée entre la réalisation d’une vente et l’encaissement des fonds correspondants par l’entreprise. Il est exprimé en nombre de jours.
Formule :
Délai de Recouvrement des Créances = (Moyenne annuelle sur 5 points des créances brutes) / (Total des ventes brutes annuelles / 365), exprimé en jours
""",
            "AM.2.2": """Le nombre de jours que représente le stock en fonction des ventes.
Formule :
Jours de Stock Disponible = [Moyenne mobile sur 15 points de la valeur brute des stocks au coût standard] / [Coût annuel des marchandises vendues (COGS)] / 365, exprimé en jours.
""",
            "AM.2.3": """ressources de transformation et le moment où les paiements doivent être effectués, exprimée en jours.
Autres termes :
Période moyenne de paiement des matières premières, Délai d’achat dans les comptes fournisseurs, Jours impayés dans les comptes fournisseurs.
Formule :
Délai de Paiement Fournisseurs = [Moyenne mobile sur 15 points des comptes fournisseurs bruts] / [Total des achats bruts annuels de matières premières / 365].

Remarque :
Le calcul de la “moyenne mobile sur 5 points” utilise à la fois des données historiques et des projections futures. Cela signifie que la moyenne mobile est calculée sur la base des quatre trimestres précédents et des prévisions pour le trimestre actuel ou suivant.
""",
            "AM.1.2": """Cette métrique mesure le rendement qu’une organisation obtient sur le capital investi dans les actifs fixes liés à la chaîne d’approvisionnement. Cela inclut les actifs fixes utilisés pour planifier, approvisionner, fabriquer, livrer et gérer les retours.
Formule :
Retour sur les Actifs Fixes de la Chaîne d’Approvisionnement = ([Revenu de la Chaîne d’Approvisionnement] - [Coût Total du Service]) / [Actifs Fixes de la Chaîne d’Approvisionnement].
""",
            "AM.2.4": """Le revenu opérationnel généré par la chaîne d’approvisionnement. Ce revenu exclut les revenus non opérationnels tels que la location de biens immobiliers, les investissements, les règlements judiciaires, la vente de bâtiments de bureaux, etc.""",
            "AM.2.5": """La somme des coûts associés aux actifs fixes impliqués dans les processus de planification, d’approvisionnement, de fabrication, de livraison et de gestion des retours""",
            "AM.1.3": """Le retour sur le fonds de roulement évalue l’importance de l’investissement par rapport à la position de fonds de roulement d’une entreprise, en comparaison avec le revenu généré par la chaîne d’approvisionnement. Les composantes incluent les comptes clients, les comptes fournisseurs, les stocks, les revenus de la chaîne d’approvisionnement, le coût des marchandises vendues (COGS) et les coûts de gestion de la chaîne d’approvisionnement.
Formule :
Retour sur le Fonds de Roulement = ([Revenu de la Chaîne d’Approvisionnement] - [Coût Total du Service]) / ([Stock] + [Comptes Clients] - [Comptes Fournisseurs]).

""",
            "AM.2.6": """Le montant des matériaux achetés, de la main-d’œuvre et/ou des ressources de conversion qui doivent être payés (comptes fournisseurs).
Formule :
Comptes Fournisseurs = [Moyenne mobile sur 15 points des comptes fournisseurs bruts], exprimée en $.

""",
            "AM.2.7": """Le montant des créances clients exprimé en dollars.
Formule :
Comptes Clients = [Moyenne mobile sur 15 points des créances brutes], exprimée en $.
""",
            "AM.2.8": """La valeur des stocks exprimée en dollars.
Formule :
Stock = [Moyenne mobile sur 5 points de la valeur brute des stocks au coût standard], exprimée en $.
""",
           "AM.3.X": """Les métriques de niveau 3 servent de diagnostics pour analyser et expliquer les métriques de niveau 2""",   
#####################################################################################################
        "Pratique émergente" : """""",
        "BP.120" : """L’impression 3D désigne le processus de création d’objets tridimensionnels à partir d’un fichier numérique à l’aide d’une imprimante de matériaux, de manière similaire à l’impression d’images sur papier. L’utilisation de machines d’impression 3D ou de prototypage rapide, qui emploient un procédé de fabrication additive, permet de transformer des conceptions issues de logiciels de conception assistée par ordinateur (CAO), de scans 3D ou de logiciels de modélisation en composants ou produits, en déposant successivement de fines couches de matériau.""",
        "BP.121" : """L’emballage numérique à la demande consiste à utiliser l’impression numérique pour créer des emballages personnalisés adaptés aux besoins spécifiques des clients et des produits. Les emballages sont imprimés et découpés numériquement selon un design défini pour chaque commande. Cette approche permet de produire des designs physiques et graphiques uniques en petites quantités. La production d’emballages à la demande en petites séries améliore l’efficacité, réduit la gestion des stocks.""",
        "BP.150" : """Un registre des risques permet de répertorier l’ensemble des expositions aux risques pour une chaîne d’approvisionnement, une fois que ces risques ont été identifiés et évalués en termes de probabilité d’occurrence et d’impact.
                    Lors de l’élaboration de ce registre, les organisations suivent souvent la pratique de regrouper les risques en catégories telles que : risques opérationnels, techniques, financiers, juridiques, liés à la marque, environnementaux, de sécurité et de santé, etc. Elles identifient ensuite les risques spécifiques à la chaîne d’approvisionnement et évaluent leur impact sur ces groupes clés.
                    Une matrice des risques est ensuite développée en plaçant la probabilité d’occurrence sur un axe et l’impact sur l’autre. Chaque risque identifié dans la chaîne d’approvisionnement est positionné sur cette matrice, ce qui permet de déterminer une note de risque pour chacun. Cette approche facilite la hiérarchisation des risques.""",
        "BP.176": """L’omni-canal est un modèle opérationnel combinant les méthodes traditionnelles de commerce de détail avec les opérations de commerce électronique. Il permet aux consommateurs d’accéder à toutes les sources d’information sur les produits et de choisir le canal de leur préférence pour les recevoir.
                   Dans le cadre de l’omni-canal, quatre éléments principaux existent :
                  a) Les lieux de stockage des stocks (ou points d’origine de la livraison) : centres de distribution, magasins de détail et fournisseurs capables d’expédier directement aux clients du détaillant.
                  b) Les points d’accès clients : où les clients passent leurs commandes et où ils reçoivent leurs marchandises, tels que les magasins, les adresses personnelles ou les points de retrait tiers.
                  c) Les flux de matériaux spécifiques : reliant les lieux de stockage et les points d’accès clients.
                  d) Les options de rapidité d’exécution des commandes : comme la livraison express (en un jour), en deux jours, ou des options plus économiques.

                  De plus, les détaillants s’efforcent d’intégrer harmonieusement leurs opérations numériques et physiques pour offrir une expérience sans couture à leurs clients. Par exemple :
	              •	Les articles achetés en ligne peuvent être retournés en magasin pour un remboursement.
	              •	Les points de fidélité sont accumulés quel que soit le canal d’achat (en magasin ou en ligne).

                   L’objectif est de garantir une expérience client cohérente, flexible et fluide à travers tous les canaux.""",
       "BP.177" : """La fabrication additive diffère de la fabrication traditionnelle en ce qu’elle crée un objet en ajoutant des couches successives de matériau, plutôt qu’en retirant de la matière comme dans les technologies de fabrication soustractive. Selon l’American Society for Testing and Materials (ASTM), la fabrication additive est définie comme un “processus d’assemblage de matériaux pour créer des objets à partir de données de modèles 3D, généralement couche par couche, contrairement aux technologies de fabrication soustractive” (source : www.astm.org).
                   Cette technologie promet de révolutionner la fabrication et de transformer fondamentalement le fonctionnement des chaînes d’approvisionnement. Bien que la fabrication additive existe depuis plus de 30 ans, elle continue d’évoluer. Beaucoup de directeurs de la chaîne d’approvisionnement considèrent cette technologie comme significative, voire perturbatrice, pour les configurations actuelles des réseaux logistiques. Cependant, nombreux sont ceux qui n’ont pas encore déterminé où et comment cette technologie pourrait être utilisée au mieux.
                 Importance stratégique :
                  Il est crucial de planifier soigneusement l’intégration de cette technologie pour résoudre les problèmes actuels de fabrication et développer des stratégies pour en tirer parti à l’avenir. Par exemple :
	           •	La Marine américaine a déployé des machines de fabrication additive à bord de ses navires pour produire les pièces nécessaires en mer.
	           •	La Station Spatiale Internationale utilise également cette technologie pour fabriquer les pièces dont elle a besoin dans l’espace.
                 Ces cas montrent le potentiel de la fabrication additive pour réduire les délais d’approvisionnement.""",
       "BP.178" : """Le terme Blockchain désigne un ensemble de technologies permettant de gérer des transactions de manière sécurisée et transparente. Il s’agit d’une pratique émergente qui suscite un intérêt croissant chez les fournisseurs et acheteurs de biens et services. Cependant, cette technologie en est encore à ses débuts de développement et d’évolution.
                  Sur une blockchain, les transactions sont enregistrées chronologiquement, formant une chaîne immuable. Selon l’implémentation, ces transactions peuvent être privées ou anonymes. Le grand avantage de la blockchain est sa structure décentralisée : le grand livre (ledger) est distribué parmi plusieurs participants dans le réseau, et non centralisé en un seul endroit. Les copies du grand livre sont simultanément mises à jour à chaque nœud actif du système.
                 Un bloc dans la blockchain peut représenter différents types de transactions et de données : monnaie, droits numériques, propriété intellectuelle, identités, titres de propriété, etc.
                  Avantages clés :
                  Cette technologie permet à chaque participant du réseau de vérifier l’intégrité du grand livre à faible coût. Cela représente un pas vers un marché décentralisé, et ouvre la voie à de nouveaux types de plateformes numériques, facilitant la confiance et la transparence dans les échanges l’autonomie opérationnelle.""",
       "BP.179" : """Le DDMRP (Material Requirements Planning piloté par la demande) est une méthode utilisée pour modéliser, planifier et gérer les chaînes d’approvisionnement afin de protéger et promouvoir le flux d’informations et de matériaux pertinents.
                    Le DDMRP sert de moteur pour la génération et la gestion des commandes d’approvisionnement dans un modèle opérationnel piloté par la demande. Cette approche permet de mieux aligner la production et l’approvisionnement avec la demande réelle, en réduisant les risques de surproduction et de ruptures de stock.""",
      "BP.180" : """Le DDS&OP (Sales & Operations Planning piloté par la demande) est un point d’intégration bidirectionnel dans un système adaptatif piloté par la demande. Il relie les plages de décisions stratégiques (annuelles, trimestrielles et mensuelles) et tactiques (horaire, quotidienne et hebdomadaire) dans le cadre de la gestion de la chaîne d’approvisionnement.
                   Le DDS&OP définit les paramètres clés d’un modèle opérationnel piloté par la demande en fonction de la stratégie d’entreprise, de l’intelligence du marché et des objectifs commerciaux principaux (informations stratégiques et exigences). Il projette également la performance du modèle basée sur ces informations et exigences stratégiques, ainsi que sur les paramètres du modèle.
                   De plus, le DDS&OP utilise l’analyse des écarts basée sur la performance passée du modèle (fiabilité, stabilité et vitesse) pour ajuster les paramètres clés du modèle opérationnel piloté par la demande et/ou recommander des ajustements stratégiques. Cela permet de projeter l’impact de ces changements sur l’entreprise, favorisant ainsi une gestion plus réactive et alignée avec les objectifs stratégiques.
                  L’Internet des Objets (IoT) fait référence au réseau d’objets physiques connectés via Internet, ainsi qu’à la communication intelligente qui s’opère entre eux. Cette technologie offre de nombreuses opportunités étendues :
              1.	Amélioration des retours clients pour le développement de produits :
               Les entreprises peuvent obtenir des informations sur les préférences des consommateurs et l’utilisation des produits, informations qui peuvent être utilisées pour améliorer les produits existants ou en développer de nouveaux. Par exemple, des capteurs placés sur des équipements peuvent permettre d’accéder à des paramètres clés de performance tels que le temps et la durée d’utilisation, la température, et les conditions de fonctionnement. Ces données peuvent ensuite être utilisées pour estimer la durée de vie restante des pièces et planifier les activités de maintenance. Cela améliorerait la maintenance basée sur les conditions réelles et augmenterait considérablement le temps de disponibilité des équipements.
	          2.	Amélioration de la performance de la chaîne d’approvisionnement :
                 L’IoT peut améliorer la performance de la chaîne d’approvisionnement dans son ensemble, grâce à l’automatisation et à une efficacité accrue des opérations, en facilitant la gestion des stocks, le suivi des livraisons et la gestion des prévisions.
               La visibilité de bout en bout est l’une des capacités clés offertes par l’Internet des Objets (IoT). En combinant des capteurs (tels que la radio-identification par fréquence (RFID)), des appareils connectés et des canaux de communication (3G/4G, GPS, Bluetooth, Internet, etc.), les entreprises peuvent surveiller en temps réel l’état du transit, y compris des facteurs tels que la localisation, la température et les diagnostics.
              Par exemple, certaines entreprises utilisent déjà cette technologie pour suivre les informations de transit en temps réel et modéliser les itinéraires idéaux afin d’optimiser la fraîcheur des marchandises périssables. Cela permet d’améliorer la gestion des stocks et de garantir que les produits arrivent dans les meilleures conditions possibles, réduisant ainsi les risques de pertes et augmentant l’efficacité globale de la chaîne d’approvisionnement.""",
      "BP.183" : """La Planification Intégrée des Affaires (IBP) est un processus et une capacité commerciale visant à maximiser la rentabilité de l’entreprise en créant un plan d’exploitation à l’échelle de l’entreprise. Ce processus guide la prise de décisions à travers tous les aspects de l’entreprise en équilibrant la demande des clients, l’approvisionnement et les ressources de l’entreprise.
                Le plan d’affaires intégré est généré avec le niveau de détail nécessaire pour que toutes les fonctions commerciales participantes puissent exécuter les activités requises pour atteindre les objectifs du plan. Il s’agit généralement d’un niveau de planification agrégée, avec la possibilité de décomposer ces informations à un niveau plus détaillé.
                L’IBP est un processus de planification à moyen terme qui se concentre sur les mois à venir, souvent jusqu’à 18 mois, au-delà de l’exercice fiscal (les délais varient selon le secteur d’activité). L’objectif du processus IBP est de parvenir à un consensus sur un plan d’affaires unique qui s’aligne avec la stratégie, les tactiques et les plans d’exécution, ainsi que les responsabilités organisationnelles et fonctionnelles.
                Le processus IBP (Planification Intégrée des Affaires) prend en compte et comprend la gestion des risques. Il est dirigé par l’équipe de direction exécutive/senior et est de nature transversale. Ce qui distingue l’IBP est l’intégration, l’implication et l’engagement appropriés des fonctions ou domaines tels que la gestion des produits, les finances, l’introduction de nouveaux produits, le marketing des produits, l’ingénierie, ainsi que le service/support, en plus des fonctions classiques de S&OP (Sales and Operations Planning) telles que les ventes, la planification de la demande/prévisions, les opérations/fabrication, et l’approvisionnement.
                Un processus IBP repose généralement sur la base d’un processus S&OP déjà établi (voir BP.021), avec des réunions de révision continues dans chaque domaine fonctionnel (produit, demande, approvisionnement, finances et prise de décision exécutive). Ce processus vise à aligner l’ensemble des fonctions pour optimiser la planification et garantir une exécution cohérente des stratégies à travers l’organisation, tout en intégrant des évaluations continues des risques et des opportunités.""",
       
       "BP.184" : """La Planification de Scénarios, également appelée analyse What-if, est un processus et une capacité analytique qui permet la prise de décisions en temps réel, stimulée par des événements. L’impact simulé sur l’entreprise et la chaîne d’approvisionnement est évalué en fonction des changements apportés à plusieurs paramètres d’entrée. Chaque combinaison de changements de paramètres et de résultats constitue un scénario. Un scénario robuste fournit un soutien à la décision en identifiant les conséquences ou les effets des événements futurs probables.
                   L’objectif ultime de la planification de scénarios est de proposer une recommandation ou une série de recommandations à exécuter, qui équilibre le mieux les compromis de la chaîne d’approvisionnement au niveau stratégique, tactique et/ou opérationnel. Les étapes du processus de planification de scénarios comprennent généralement les activités suivantes :
                	1.	Définir l’événement déclencheur,
                	2.	Analyser les résultats possibles,
	                3.	Développer les réponses recommandées,
	                4.	Examiner et approuver les réponses recommandées,
	                5.	Surveiller les événements et exécuter la réponse.
                  Ce processus permet d’anticiper les futurs défis ou opportunités et de préparer des actions adaptées pour réagir de manière proactive aux changements ou imprévus dans la chaîne d’approvisionnement. Le résultat de la Planification de Scénarios est une décision holistique, accompagnée de responsabilités assignées et d’un résultat commercial spécifique. Il s’agit d’une pratique émergente qui peut être appliquée dans les processus S&OP (Sales and Operations Planning) et Planification Intégrée des Affaires (IBP). Cette pratique est continuellement revue par rapport aux indicateurs menants (leading indicators) et retardés (lagging indicators).
               En intégrant la planification de scénarios dans ces processus, les entreprises peuvent mieux anticiper les changements du marché et ajuster leurs stratégies de manière proactive, en équilibrant les risques et les opportunités, et en assurant une exécution efficace à travers toutes les fonctions organisationnelles.""",
        "BP.188" : """ La capacité de suivre un objet tout au long de son cycle de vie à travers une chaîne d’approvisionnement est un élément fondamental dans la création de visibilité afin d’obtenir un contrôle sur la chaîne d’approvisionnement. L’objectif est de créer une synchronisation des objets, du Vente au Cash, afin de permettre l’intégration des systèmes et la digitalisation.
                  La méthode pour décrire ces liens entre objets est souvent appelée correspondance à 3 voies (3-way match) ou correspondance à 4 voies (4-way match). Ce processus permet de relier des informations à chaque étape du cycle de vie d’un produit ou service, garantissant ainsi la transparence et l’efficacité de la chaîne d’approvisionnement. Cela permet de vérifier que les commandes, les réceptions de marchandises et les paiements sont cohérents et bien synchronisés à travers les différents.""",
       
      "Meilleures pratiques":"""Les meilleures pratiques sont des pratiques "actuelles", "structurées" et "répétables" qui ont eu un impact positif prouvé sur la performance de la chaîne d'approvisionnement :
                           Actuelles : Pas émergentes, pas obsolètes.
                           Structurées : Elles comportent un objectif clairement défini, un périmètre, un processus et une procédure.
                           Prouvées : Démontrées dans un environnement de travail, et liées à des indicateurs clés.
                           Répétables : Prouvées dans plusieurs organisations et industries.
                          Les meilleures pratiques SCOR ont été choisies par des praticiens SCOR dans divers secteurs. Il est entendu que toutes les meilleures pratiques ne donneront pas les mêmes résultats pour toutes les industries ou chaînes d'approvisionnement.
                          Investissement, Risque : Modéré, Résultats : Modérés.
                        Ce qui suit n'est qu'une liste partielle des meilleures pratiques SCOR et inclut uniquement des définitions partielles du cadre SCOR.""",


         "BP.002" : """Les stratégies de gestion des risques sont développées et communiquées. Les stratégies couramment utilisées incluent la réduction des risques, l'évitement des risques, le transfert des risques et l'acceptation des risques.
                      Réduction des risques (Risk Mitigation) : Plan visant à réduire la probabilité d'occurrence ou à minimiser l'impact du risque.
                      Évitement des risques (Risk Avoidance) : Action entreprise lorsque les risques de la chaîne d'approvisionnement sont trop élevés, en termes de probabilité d'occurrence et d'impact, et dépassent les limites acceptables définies par l'organisation.
                      Transfert des risques (Risk Transfer) : Transfert partiel ou total du risque vers un autre processus où il peut être mieux géré ou atténué par des actions moins coûteuses.
                      Acceptation des risques (Risk Acceptance) : Décision prise lorsqu'un risque a une faible probabilité d'occurrence et un impact limité, et qu'un plan de contingence est facilement déployable en cas de survenance du risque.
                      Les stratégies de gestion des risques peuvent varier selon la chaîne d'approvisionnement.""",
          "BP.003" : """Il s'agit de la pratique consistant à prendre des décisions de disposition pour les pièces réparables, les noyaux ou les carcasses dès le début du processus d'autorisation de retour de matériel (RMA). Les instructions pour ces décisions doivent être incluses dans l'autorisation fournie aux clients responsables de l'expédition et aux parties prenantes internes responsables de la réception. Les décisions d'acheminement sont également prises et incluses dans ces instructions. Des critères tels que des délais longs, une forte demande ou des priorités sont appliqués, ce qui entraîne une induction automatique dans le processus de Maintenance, Réparation et Opérations (MRO), un acheminement vers un lieu de stockage ou une élimination.""",
          "BP.103" : """Également appelée rationalisation des SKU (Unités de Stock) ou des produits, la rationalisation des articles implique la prise de décisions concernant l’ajout, la suppression ou le maintien de produits, services ou fonctionnalités dans une offre de portefeuille. Certaines stratégies prévoient que ces décisions soient prises au niveau des familles de produits.
                       La rationalisation doit tenir compte du stade de fabrication auquel l'article est personnalisé ainsi que de la proximité avec la commande du client, afin d'optimiser les coûts opérationnels et la complexité. Compte tenu des multiples facteurs et compromis impliqués dans ces décisions, la rationalisation des articles doit être considérée comme un élément, mais non un substitut, d’une approche plus globale de gestion de la complexité de la chaîne d’approvisionnement. (Suite dans le cadre de travail).""",
          "BP.016" : """Simuler et mettre en œuvre des décisions de planification tactique et d'approvisionnement basées sur un modèle unique, globalement cohérent. La planification du réseau d'approvisionnement permet aux organisations de créer une correspondance étroite entre l'offre et la demande en intégrant l'achat, la fabrication, la distribution et le transport dans un modèle cohérent. En modélisant l'ensemble du réseau d'approvisionnement et les contraintes associées, il devient possible de synchroniser les activités et de planifier le flux de matériaux dans toute la chaîne d'approvisionnement. Les résultats sont des plans réalisables pour l'achat, la fabrication, l'inventaire et le transport. Ce processus permet également aux organisations de déterminer de manière dynamique comment et quand les stocks doivent être distribués. Le système de support optimise les plans de déploiement en fonction des algorithmes disponibles, ainsi que des règles et politiques utilisateur.""",
          "BP.024" : """L'optimisation de la chaîne d'approvisionnement fait partie du plan stratégique des entreprises à la pointe de leur secteur. Elle permet à la direction générale de repenser la chaîne d'approvisionnement dans le cadre de la stratégie globale de l'entreprise, en réponse à des changements réels ou anticipés du marché.
                      Sur la base de données réelles ou de projections d'analystes (par exemple : le baril de pétrole atteindra 120 dollars), les entreprises effectuent plusieurs simulations informatiques pour rechercher une solution optimale concernant :
                     Les emplacements des fournisseurs,
                     Les niveaux de stock,
                     Les coûts de transport à l'échelle mondiale,
                     La gestion du cycle de vie des produits (de l'introduction de nouveaux produits à la fin de vie),
                     Les emplacements des centres de distribution,
                     Les impacts environnementaux (empreinte carbone).
                     (Suite dans le cadre de travail).""",
          "BP.025" : """La soumission de réclamations de garantie en libre-service permet aux clients et aux prestataires de services de déposer leurs réclamations de garantie via le web, réduisant ainsi la charge de travail interne liée à la validation et au traitement.
                     Cela peut être réalisé par le biais d'un chargement par lots de plusieurs réclamations simultanées ou d'une soumission individuelle, une réclamation à la fois. Les informations collectées lors de la soumission permettent une analyse et un traitement ultérieurs.
                    Les résultats de l'analyse peuvent être mis en ligne, accessibles selon les niveaux d'accès définis, afin que ces informations puissent être transmises aux autorités compétentes si nécessaire. De plus, l'approbation et le paiement automatiques de certaines réclamations peuvent être envisagés si elles répondent à des critères spécifiques.""",
          "BP.026" : """Mettre en place un processus mensuel rigoureux et interfonctionnel pour :
                      Améliorer la précision de la gestion de la demande (prévisions),
                      Définir une politique d'inventaire adaptée à l'entreprise,
                      Établir un consensus sur l'équilibre entre la demande et l'offre.""",
          "BP.027" : """Le réapprovisionnement basé sur la demande (« pull ») est une approche qui s'appuie sur la demande client pour remplacer et optimiser les stocks tout en réduisant les coûts totaux d'approvisionnement. Cette pratique est reconnue depuis des décennies pour son efficacité.
                       Avec une approche basée sur la demande, le signal pour réapprovisionner les stocks en aval est déclenché par la demande ou l'utilisation réelle, plutôt que par une prévision qui pousse les produits et les matériaux dans la chaîne d'approvisionnement. Cette méthode s'appuie sur l'analyse des variations historiques entre la demande prévue et la demande réelle des clients pour déterminer les niveaux de stock appropriés.""",
          "BP.028" : """Utilisation de l'optimisation stochastique à plusieurs niveaux (simultanée sur tous les points de stockage des stocks dans la chaîne d'approvisionnement). Traditionnellement utilisée pour le réapprovisionnement basé sur les prévisions, comme alternative au réapprovisionnement basé sur la méthode du tirage (Pull-Based Replenishment), mais elle peut également être utilisée pour calculer le point de commande (Reorder Point).""",
          "BP.029" : """Les chaînes d'approvisionnement et les réseaux d'approvisionnement décrivent tous deux le flux et le mouvement des matériaux et des informations, en reliant les organisations pour servir le client final. L'optimisation de la stratégie du réseau peut être utilisée pour déterminer les emplacements optimaux de fabrication et d'entreposage en se concentrant sur la réduction des coûts totaux de la chaîne d'approvisionnement (généralement axée sur la réduction des coûts de transport). Cela se fait en examinant un réseau de chaîne d'approvisionnement des entreprises fournissant des produits et celles en contact avec le marché afin de consolider les emplacements de stockage des stocks.""",
          "BP.031" : """Pratique de réduction des stocks visant à déterminer quels SKUs peuvent être supprimés en utilisant l'Analyse du Coût des Ventes des SKUs. Cela peut nécessiter de travailler avec les clients pour évaluer la possibilité de passer à un autre SKU ou prendre la décision d'abandonner un SKU en raison de faibles ventes.""",
          "BP.034" : """La planification collaborative des stocks peut être utilisée pour étendre la planification de la chaîne d'approvisionnement avec les clients clés. Cela peut se faire à travers une réunion conjointe de Planification des Ventes et des Opérations (S&OP) entre chaque client clé et fournisseur pour discuter de la gestion de la demande et de l'approvisionnement à travers l'entreprise étendue (clients clés).
                      La planification S&OP inclura l'examen de la demande historique et future des clients, la précision des prévisions de la demande, les pannes prévues par client ou fournisseur, la planification à long terme, etc.
                      La prévision collaborative consiste à ce que les membres de la chaîne d'approvisionnement maintiennent et mettent à jour conjointement un processus unique de prévision dans le système.
                     Ainsi, les informations de prévision deviennent centralisées.""",
          "BP.041" : """Évaluer la possibilité de changer le mode de transport entrant/sortant vers un mode plus rapide en fonction des conditions de fret (FOB, etc.) pour accélérer le transfert de la propriété des stocks au client et/ou mieux aligner la demande et l'approvisionnement afin d'optimiser les niveaux de stocks. Cela peut être combiné avec d'autres opportunités telles que le changement de la décision de sourcing vers des points de stockage locaux (réduire le temps de cycle), et le pooling des risques.""",
          "BP.048" : """Équilibrer le coût/la valeur de l'offre de réductions aux clients pour avancer les commandes sur des produits finis spécifiques en inventaire. Cela nécessiterait un processus et des outils pour identifier et analyser la proposition de valeur / le compromis. Il peut être possible de tirer parti des outils commerciaux pour analyser les incitations au paiement ; cela peut être combiné avec d'autres opportunités telles que l'intégration des objectifs de gestion des stocks dans les équipes commerciales ou l'accélération des expéditions sortantes aux clients.""",
          "BP.049" : """Les modèles prédictifs appropriés sont essentiels pour pouvoir gérer de manière proactive les problèmes émergents, plutôt que de réagir face aux jalons manqués. La planification Lean crée des plans de projet réalistes qui modélisent le projet de manière robuste, depuis le début jusqu'à la livraison finale. Commencer par le livrable final est la meilleure façon de créer un plan tactique. La planification Lean identifie le flux d'informations entre les tâches et fait remonter cette information tâche par tâche durant le processus de planification, créant ainsi un modèle de projet robuste qui identifie TOUT le travail qui doit être accompli pour atteindre le livrable final du projet. (Suite dans le cadre de référence).""",
          "BP.052" : """Modifier le processus de développement de nouveaux produits pour intégrer la réutilisation et/ou l'évaluation des risques liés à la gestion des stocks (par exemple, inclure une validation de la chaîne d'approvisionnement sur l'impact potentiel de la gestion des stocks du développement d'un nouveau produit proposé). Cela pourrait inclure une fin de cycle de vie obligatoire pour un autre produit, l'accord commercial sur l'exposition potentielle aux stocks/capital de travail, etc.""",
          "BP.053" : """Cette pratique inclut l'utilisation d'outils de fiabilité et la mise en place de rôles dans les processus de travail au sein de la production pour améliorer la fiabilité de la fabrication. Elle intègre l'analyse et la simulation du processus de production afin d'identifier des opportunités pour accroître la fiabilité des équipements et améliorer les coûts de production, la capacité et les facteurs de service.""",
          "BP.055" : """La pratique des évaluations formelles de la performance des transporteurs afin de réduire les risques de variations du budget des coûts d'acheminement. Une évaluation formelle de la performance des transporteurs est cruciale, car les partenaires de transport représentent l'interface entre le fournisseur et le client. La qualité de la livraison à temps et en bon état a un impact énorme sur la satisfaction des clients, les taux de retour et les ventes répétées. Un programme d'évaluation des transporteurs doit inclure une liste complète de critères d'évaluation pour refléter la performance globale du service et les objectifs d'amélioration des coûts. Les critères d'évaluation devraient inclure des mesures quantitatives ainsi que qualitatives. Les critères quantitatifs peuvent inclure la performance de livraison à temps, les ratios de réclamations, la précision de la facturation, la performance des coûts et d'autres critères mesurables. Les mesures qualitatives peuvent inclure la réactivité des conducteurs et des représentants commerciaux, la qualité du service client, les enquêtes auprès des parties prenantes, les plaintes des clients ou d'autres évaluations basées sur la valeur. (Suite dans le cadre de référence.""",
          "BP.062" : """Re-valider les données maîtres existantes (délais de commande, délais de réapprovisionnement, délais de transit, etc.) pour s'assurer qu'elles correspondent aux capacités et performances opérationnelles actuelles.
                        Ces informations sont utilisées pour le point de commande des stocks et la fixation des objectifs afin de déterminer la taille/la fréquence du réapprovisionnement des stocks. C'est une étape critique dans la gestion des stocks et nécessite une discipline mensuelle pour suivre cela en raison du nombre de processus/systèmes qui dépendent de ces informations comme variables clés d'entrée.
                        Établir des rôles/responsabilités/comptes rendus clairs pour la gestion des données maîtres ; une condition préalable essentielle pour un large éventail d'opportunités en gestion des stocks.
                        Cela peut être combiné avec d'autres opportunités telles que le réapprovisionnement basé sur le tirage (Pull-based Replenishment).""",
          "BP.071" : """Équilibrer le compromis entre la réduction des coûts logistiques et l'augmentation des coûts en capital.
                       Les facteurs incluent la taille des lots d'expédition, les coûts de préparation par expédition, la consommation/demande des matières premières et la capacité de stockage afin d'identifier la capacité de stockage appropriée pour minimiser les coûts de transport.""",
          "BP.074" : """L'alignement des mesures fait référence au développement organisé et délibéré des métriques à travers une organisation. Le processus commence par les métriques organisationnelles/entreprises ou de la chaîne d'approvisionnement, puis se décompose en processus organisationnels de niveau 2, niveau 3, et au-delà si nécessaire. Voici les traits clés qui définissent de bonnes métriques :
                       Aligner avec la stratégie de la chaîne d'approvisionnement et de l'entreprise
                       Avoir une ligne claire vers le client ou l'objectif commercial
                       Fournir une vue équilibrée de la performance
                       Mesurer de manière implacable la vérité
                       Basées sur les données
                       Être actionnables
                       Répondre aux questions :
                       Où en sommes-nous actuellement ?
                       Où devons-nous être ?
                      L'alignement des métriques peut être réalisé en suivant ces étapes :
                      Définir les chaînes d'approvisionnement en utilisant la méthodologie SCOR. Cela implique généralement de créer une matrice de familles de produits versus groupes de clients (exemple).""",

       "Pratique standard" : """Les pratiques standard sont celles par lesquelles un large éventail d'entreprises a historiquement fonctionné par défaut ou par hasard. Ces pratiques bien établies accomplissent le travail, mais ne fournissent pas un avantage concurrentiel ou une réduction significative des coûts par rapport à d'autres pratiques (sauf par rapport aux pratiques en déclin).
                               Investissement, Risque : Faible, Résultats : Faibles.
                               Ce qui suit n'est qu'une liste partielle des pratiques standard SCOR et inclut uniquement des définitions partielles du cadre SCOR.""",
       
           "BP.001" : """La gestion des risques de la chaîne d'approvisionnement est l'identification, l'évaluation et l'atténuation systématiques des disruptions potentielles dans les réseaux logistiques, dans le but de réduire leur impact négatif sur la performance du réseau logistique.
                       Un grand nombre de disruptions potentielles peut avoir un impact négatif sur la performance de la chaîne d'approvisionnement. Ces disruptions peuvent survenir à l'intérieur de la chaîne d'approvisionnement (par exemple, qualité insuffisante, fournisseurs peu fiables, pannes de machines, demande incertaine, etc.) ou à l'extérieur (par exemple, inondations, terrorisme, grèves, catastrophes naturelles, etc.). Les deux types de risques sont abordés dans une approche intégrée en trois phases pour la gestion des risques de la chaîne d'approvisionnement.
                      (Suite dans le cadre de référence).""",
           "BP.004" : """La priorisation du réseau pour l'identification des risques est le processus qui consiste à prioriser les parties d'une chaîne d'approvisionnement pour l'analyse des risques, en fonction du potentiel global de risque dans chaque portion de la chaîne d'approvisionnement. La priorisation est généralement basée sur la criticité du composant ou du produit circulant dans une partie de la chaîne d'approvisionnement pour votre entreprise et sur le nombre de sources pour le matériau circulant dans cette portion de la chaîne d'approvisionnement.""",
           "BP.005" : """Il s'agit de la pratique où un client génère les factures pour les produits ou services qu'il a consommés auprès d'un fournisseur. L'avantage de ce processus pour l'entreprise qui s'auto-facture est que les processus de réconciliation — tels que la vérification à trois voies avant le paiement des factures — ne sont plus nécessaires. (Les processus de réconciliation sont transférés au fournisseur.) Une application courante de ce processus est l'auto-facturation pour les services de transport et les matériaux consommés à partir des stocks appartenant au fournisseur ou en consignation.
                        Conditions pour l'auto-facturation :
                   Des accords de niveau de service clairs entre le fournisseur et le client pour le produit ou le service.
                   Des méthodes claires pour mesurer le niveau et la qualité des services fournis ou des matériaux consommés.
                   Des processus définis et convenus pour la gestion des enregistrements, les rapports et les réclamations.
                   Des normes pour la communication des données électroniques entre le fournisseur et le client (EDI).
                   Les stocks en consignation ne sont pas une condition préalable pour l'auto-facturation.
                   Les matériaux commandés (appelés sur un contrat-cadre) peuvent également être éligibles à l'auto-facturation.
                   Noms alternatifs : Auto-billing.""",
          "BP.006" : """L'organisation des processus de sourcing où le transfert de propriété des matériaux est basé sur un signal plus bas dans la chaîne d'approvisionnement (par exemple, la fabrication ou la livraison).
                    Alors que le transfert de propriété pour les stocks « réguliers » est déclenché par la réception et/ou la vérification de l'état des matériaux reçus, la pratique des stocks en consignation est conçue pour retarder le transfert de propriété jusqu'à la réalisation d'une activité telle que l'assemblage, la production ou l'expédition au client.
                    L'application des stocks en consignation ne réduit pas par défaut l'inventaire physique ; elle affecte la propriété des stocks.
                    La mise en œuvre des stocks en consignation permet de libérer des liquidités.
                    Noms alternatifs : Stocks appartenant au fournisseur (Supplier Owned Inventory - SOI), Stocks appartenant au fournisseur (Vendor Owned Inventory - VOI).""",
         "BP.007" : """Pour éviter les situations de surstock, nous révisons régulièrement les niveaux d'inventaire de référence. L'inventaire de référence est défini comme le niveau de stock le plus bas qu'un SKU particulier ait effectivement eu au cours des 12 derniers mois. Cela signifie qu'il y aura un inventaire de référence pour tous les articles qui n'ont pas eu de rupture de stock.
                    Au maximum, l'inventaire de référence devrait correspondre au stock de sécurité. S'il est nettement supérieur au stock de sécurité (le stock de sécurité n'étant jamais effectivement utilisé), les paramètres de planification et les tampons dans le système doivent être révisés.
                    Pour évaluer l'ensemble d'une gamme de produits, nous calculons la valeur totale agrégée de l'inventaire de référence. La métrique est exprimée en valeur totale, en nombre d'articles concernés et en pourcentage de la valeur totale du stock.
                    (Suite dans le cadre de référence).""",
         "BP.008" : """Pour éviter les situations de surstock, nous examinons régulièrement les niveaux de stocks lents. Un stock lent est défini comme la valeur des SKUs dont le niveau de stock est supérieur à la consommation totale au cours des 12 derniers mois. Les stocks lents peuvent résulter de diverses raisons. Dans la plupart des cas, des contraintes en termes de temps et de quantité d'approvisionnement ne correspondent pas à la demande du côté commercial (telles que des tailles de lots minimales, des équipements contraints, des pénuries attendues de matières premières, etc.).
                   Pour évaluer une gamme de produits entière, nous calculons la valeur totale agrégée des stocks lents. La métrique est exprimée sous forme de valeur totale, du nombre d'articles affectés et en pourcentage de la valeur totale des stocks.
                  (Suite dans le cadre de référence).""",
         "BP.009" : """Une technique de réapprovisionnement des stocks où un matériau est réapprovisionné en fonction de sa consommation. Aujourd'hui, le Kanban peut être mis en œuvre en utilisant différentes "solutions technologiques", mais un exemple classique de Kanban est le système à deux bacs : un bac est situé au point de consommation (par exemple, sur le plancher de production), le second bac est en cours de remplissage et placé derrière le premier.
                    Une fois que le premier bac est épuisé, il est envoyé pour être rempli et le second bac devient le premier bac. Voir l'illustration.
                    Exemple de formule pour calculer la taille du bac dans un système à deux bacs :
                    Taille minimale du bac = [consommation projetée par unité de temps] * [temps de cycle pour le réapprovisionnement en unités de temps] / [nombre de bacs] = 100 par jour * 3 jours / 2 bacs = 150.
                    (Suite dans le cadre de référence).""",
         "BP.010" : """Il s'agit d'une pratique de réapprovisionnement des stocks où des demandes d'achat ou des bons de commande sont créés lorsque le stock d'un article tombe en dessous du niveau minimum. La quantité de la demande ou de la commande ramènera l'inventaire au niveau maximum. Les méthodes de réapprovisionnement Min-Max sont généralement mises en œuvre par automatisation. Plusieurs options de configuration existent pour le réapprovisionnement Min-Max : • Le réapprovisionnement Min-Max physique prend uniquement en compte l'inventaire disponible, les commandes clients existantes ne sont pas incluses dans les calculs. Cela présente des caractéristiques proches d'un système Kanban. • Le réapprovisionnement Min-Max logique soustrait les commandes clients de l'inventaire disponible. Si cet inventaire net des commandes est inférieur à la quantité minimale de commande, une demande ou une commande sera créée. Cela correspond aux pratiques Available-to-Promise (ATP) ou Capable-to-Promise (CTP). Les détails supplémentaires peuvent inclure la soustraction uniquement des commandes "propres" ou de toutes les commandes. (Les commandes "propres" sont celles qui ne sont pas en attente d'une action client, comme un blocage de crédit, etc.) Le calcul du niveau minimum inclut le temps de cycle de réapprovisionnement et un tampon (pour la variabilité de la demande et du temps de cycle). Le niveau maximum est de préférence le niveau minimum plus la quantité économique de commande (EOQ - Economic Order Quantity). En général, le réapprovisionnement Min-Max nécessite l'automatisation des processus. Le réapprovisionnement est déclenché par l'exécution d'un programme ou d'un rapport de replanification.
                    Nom alternatif : Système de point de commande.""",
         "BP.011" : """Il s'agit de la pratique consistant à commander, expédier, recevoir et/ou stocker les matériaux dans le même ordre que celui dans lequel ils seront consommés.
                    Les matériaux sont généralement configurables ou ont de nombreuses variantes (exemple : teintes de couleur). Cette pratique peut être appliquée dans les processus sur site et dans les processus de fournisseur à fabricant.
                    Processus sur site : Les matériaux sont prélevés à partir d'un emplacement de stockage (tel qu'un entrepôt de matières premières) dans l'ordre exact du planning de production/de la ligne et livrés au point d'utilisation (pick-to-sequence). L'opérateur doit utiliser les matériaux dans l'ordre dans lequel ils ont été fournis. Cela peut s'appliquer aux matériaux sourcés via les processus S1, S2 et S3.
                    Processus fournisseur-à-fabricant : Les matériaux sont commandés auprès du fournisseur dans l'ordre (order-in-sequence). Le fournisseur traite la commande et charge le véhicule de transport dans l'ordre (ship-to-sequence). Les matériaux sont ensuite déchargés et livrés au point d'utilisation (receive-to-sequence).
                    Cette version s'applique uniquement aux approvisionnements S2 et S3.""",
         "BP.012" : """Il s'agit de la pratique consistant à stocker des informations sur l'historique et/ou la généalogie d'un produit ou d'un matériau. Cela peut inclure des informations telles que son origine, les différents matériaux utilisés pour le fabriquer, la qualité des matériaux et d'autres informations liées à la généalogie du produit.
                    Le suivi des lots repose sur trois exigences fondamentales :
                    Un moyen d'identifier le lot ou le numéro de série (identifier)
                    Un système pour enregistrer les étapes clés pour chaque lot ou numéro de série (enregistrer)
                    Un processus pour récupérer les informations par lot ou numéro de série (afficher)
                    Le suivi des lots peut faire usage de codes-barres, de puces RFID ou d'autres méthodes visuelles ou électroniques pour identifier le lot.
                    Les systèmes ERP modernes offrent généralement des fonctionnalités d'enregistrement et d'affichage des lots.
                    Du matériel et des instructions pour les opérateurs/manutentionnaires peuvent être nécessaires pour lire les identifiants des lots et communiquer l'événement/étape clé au système d'enregistrement (ERP).""",
         "BP.014" : """La planification de la demande et la prévision : Utilisation des algorithmes de prévision de pointe pour la planification du cycle de vie des produits et la planification des promotions commerciales. Comprendre et prédire la demande des clients est essentiel pour les fabricants et les distributeurs afin d'éviter les ruptures de stock et de maintenir des niveaux de stock adéquats. Bien que les prévisions ne soient jamais parfaites, elles sont nécessaires pour se préparer à la demande réelle. Afin de maintenir un inventaire optimisé et une chaîne d'approvisionnement efficace, des prévisions de demande précises sont impératives, accompagnées des algorithmes les plus avancés. Ces algorithmes sont au cœur des solutions de gestion de la demande et de l'approvisionnement. Ils permettent de travailler sans difficulté à tout niveau d'agrégation et sur n'importe quelle dimension (produit, canal ou client) avec fluidité et performance, sans avoir besoin de pyramides de prévision rigides.""",
         "BP.015" : """Atteindre les niveaux de service client souhaités tout en maintenant une quantité minimale de stock de sécurité. Les méthodes standards de planification du stock de sécurité sont utilisées pour constituer le stock disponible en fonction des valeurs de stock de sécurité que les entreprises définissent dans leur master produit par emplacement, en fonction de l'expérience passée. Contrairement à la planification du stock de sécurité basée sur des modèles, les erreurs de prévision ne sont pas prises en compte lorsqu'elles utilisent les méthodes standard. Les valeurs de stock de sécurité peuvent être maintenues comme une valeur statique ou dépendante du temps. Les méthodes avancées de planification du stock de sécurité sont utilisées pour calculer le stock de sécurité dépendant du temps pour les produits finis et les composants. Dans ce type de planification, le système prend en compte les prévisions de demande et les erreurs de prévision au sein de la chaîne d'approvisionnement.""",
         "BP.017" : """Déterminer la meilleure stratégie à court terme pour répondre à la demande et approvisionner les points de stockage. La planification de la distribution permet à l'utilisateur de définir certains paramètres de contrôle des stocks (comme un stock de sécurité) et de calculer les besoins en stocks à échéances temporelles. Ce processus est également couramment appelé Planification des besoins en distribution (DRP).""",
         "BP.018" : """Le système de classification ABC est une analyse de Pareto d'une gamme d'articles en stock, répartis en trois ou quatre catégories. Le système ABC nécessite des niveaux de contrôle des stocks différents pour chaque catégorie. Une méthode de calcul courante consiste à utiliser le coût standard multiplié par la quantité utilisée par période. Le système peut être structuré de manière aussi simple que suit :
                    Calculer la dépense prévisionnelle sur 12 mois (au coût standard) pour tous les composants de stock.
                    Classer les articles par ordre décroissant.
                    Les articles "A" représentent les articles les plus utilisés et doivent compter pour 70-80 % de l'utilisation totale.
                    Les articles "B" représentent les 15-20 % suivants de l'utilisation annuelle totale.
                    Les articles "C" sont les articles restants, représentant les 5-10 % restants.
                    Les stocks excédentaires et obsolètes encore en stock peuvent être étiquetés comme "D".""",
        "BP.021" : """Est une pratique de planification à moyen et long terme de la chaîne d'approvisionnement qui vise à comparer le plan de ventes prévisionnelles aux ressources de l'entreprise (capacité de production, personnel, matières premières) et à analyser où des déséquilibres peuvent exister par rapport au plan. Cette pratique continue est réalisée mensuellement et se projette sur les 12 mois à venir de manière glissante. Le focus est généralement placé sur les mois deux ou trois, car le mois immédiat est considéré comme déjà planifié. (Les délais varient en fonction du secteur industriel). Il s'agit d'un outil stratégique, normalement révisé par l'équipe de direction/senior, qui prend des décisions pour résoudre les déséquilibres, tels que les modifications des horaires de travail, l'ajustement du personnel ou des politiques de gestion des stocks.""",

###############################################################################################################################

            "Compétences": """Dans le cadre SCOR complet, chaque compétence a une définition et répertorie les processus, pratiques, expériences et formations SCOR associés.Les éléments associés ne sont pas inclus dans cette application. La compétence est la capacité à fournir des résultats prédéterminés avec un minimum de temps et d'énergie. Les compétences sont définies davantage par les expériences, les formations et les niveaux de compétences. Des exemples de compétences en matière de chaîne d'approvisionnement comprennent : la planification générale, les réglementations d'importation/exportation, la planification de la production et l'atténuation des risques. Les compétences sont codées dans le cadre SCOR comme"HS.000". (Ceci n'est qu'une liste partielle de Compétences SCOR).""",

	         "HS.002": "Connaissance pratique des tests fonctionnels et/ou des tests d’assurance qualité d’un produit pour garantir qu’il répond aux spécifications contractuelles prévues concernant sa forme, son ajustement et sa fonction. Les tests d’acceptation peuvent parfois être réalisés dans les installations du fournisseur et/ou au lieu de livraison final du client. La réussite des tests d’acceptation du produit peut être une condition préalable au paiement du fournisseur.",
	         "HS.003": "Le processus de collecte, d’analyse et de communication des informations financières concernant une entité commerciale à des parties prenantes spécifiées.",
	         "HS.004": "Connaissance des techniques de communication efficaces en approvisionnement ou en développement commercial pour informer et/ou solliciter les fournisseurs potentiels concernant les spécifications des produits ou services.",
	         "HS.005": "L’agencement des travailleurs, des machines et des équipements dans lequel le produit en cours d’assemblage passe successivement d’une opération à l’autre jusqu’à sa finition.",
	         "HS.006": "Le processus (qui nécessite l’utilisation de tableurs ou de logiciels) permettant d’identifier, de collecter, de maintenir et de suivre les actifs de l’entreprise.",
	         "HS.007": "Le processus de gestion et d’allocation des ressources et des stocks disponibles (à différents niveaux) en fonction des règles commerciales. Cela inclut la gestion des dates, des délais, des capacités et des stocks.",
	         "HS.009": "Connaissance de base du concept d’application ou d’incorporation sur/into un produit d’une représentation optique lisible par machine des données (code-barres) et/ou de l’utilisation des ondes radio avec des étiquettes d’identification par radiofréquence (RFID) dans le but d’identifier et de suivre ce produit.",
	         "HS.012": "Connaissance pratique du processus de capture et de comparaison des processus commerciaux et des mesures de performance de son propre entreprise avec ceux des pairs de l’industrie et/ou des meilleures pratiques d’autres industries. Les mesures typiques incluent la qualité, le temps et les coûts, dans le but de réduire les écarts de performance et d’améliorer l’efficacité.",
	         "HS.0015": "Le processus d’utilisation de la technologie informatique pour aider à la conception, à l’analyse et à la fabrication de produits.",
	         "HS.0016": "Le processus de détermination et de gestion de la capacité de production nécessaire à une organisation pour répondre aux demandes changeantes de ses produits.",
	         "HS.0018": "Sélection d’un mode de transport et d’un prestataire de services afin de respecter les délais, les coûts et les objectifs de service.",
	         "HS.0139": "Connaissance pratique du processus d’approvisionnement consistant à demander et recevoir des offres/devis de fournisseurs, entrepreneurs ou prestataires concurrents, en fonction des numéros de pièces de produits, de la portée, des spécifications, des termes et conditions, et dans certains cas, des critères d’évaluation des offres.",
	         "HS.0022": "Expérience dans le processus de sollicitation, l’évaluation des offres/propositions, l’attribution du contrat, la gestion post-attribution et la clôture. Une telle connaissance est nécessaire pour la mise en place de ces accords dans l’ensemble des fonctions d’approvisionnement.",
	         "HS.0025": "Un ensemble documenté de principes de base et de lignes directrices associées, formulé et appliqué par l’organe de gouvernance ou un comité désigné d’une organisation, qui dirige et limite les décisions et actions d’une entreprise dans la poursuite de ses objectifs.",
	         "HS.0028": "Le processus ou le flux de travail associé à l’identification, la réception, l’acceptation, le prélèvement, l’emballage, la livraison et l’expédition des articles emballés vers un transporteur.",
	         "HS.0029": "Le processus de gestion des relations et des interactions d’une entreprise avec ses clients et prospects commerciaux, incluant éventuellement la synchronisation des processus métier dans le but d’identifier, d’attirer et de gérer les clients nouveaux et existants.",
	         "HS.0032": "Processus de transfert d’informations entre le client et le fournisseur par parole ou par écrit.",
	         "HS.0124": "Connaissance pratique des processus nécessaires pour développer, exécuter et maintenir des plans, politiques, programmes et pratiques qui contrôlent, protègent, livrent et améliorent la valeur des données et des systèmes d’information/actifs.",
	         "HS.0036": "Connaissance de base de la planification et de la gestion des livraisons de produits sourcés afin de répondre aux exigences de réapprovisionnement des stocks ou des plans de production programmés.",
	         "HS.0037": "Le processus de gestion de la fabrication par lequel les matières premières et la capacité de production sont allouées de manière optimale pour répondre à la demande.",
	         "HS.0069": "Le processus de planification, mise en œuvre et contrôle du flux avant et arrière, ainsi que du stockage des biens, services et informations connexes entre le point d’origine et le point de consommation, afin de répondre aux exigences des clients et ainsi ajouter de la valeur pour le client.",
	         "HS.0094": "Connaissance pratique du processus d’acquisition de biens et/ou de services au meilleur coût total de possession, en quantité et qualité appropriées, au bon moment et au bon endroit, avec toute la documentation requise. Cela peut inclure des achats simples et répétitifs de type “Make-to-Stock” ou des produits plus complexes “Make-to-Order” ou “Engineer-to-Order”.",
	         "HS.0108": "La structure organisationnelle, les procédures, les processus et les ressources nécessaires à la mise en œuvre de la gestion de la qualité.",
	         "HS.0121": "Un système pour gérer les retours de produits défectueux.",
	         "HS.0124": "L’identification, l’évaluation et la hiérarchisation des risques et des exceptions, suivies de l’application coordonnée et économique des ressources pour minimiser, surveiller et contrôler la probabilité et/ou l’impact des événements malheureux.",
	         "HS.0139": "Le processus de collaboration avec les fournisseurs essentiels au succès de l’organisation pour maximiser la valeur potentielle de ces relations.",
	         "HS.0144": "Le processus consistant à ajouter ou à renforcer la sécurité de la chaîne d’approvisionnement. Il combine les pratiques traditionnelles de gestion de la chaîne d’approvisionnement avec les exigences de sécurité du système, lesquelles sont dictées par des menaces telles que le terrorisme, la piraterie et le vol.",
	         "HS.0165": "Connaissance et expérience dans la coordination et la surveillance des changements apportés aux processus métier, applications, équipements, ressources, systèmes d’exploitation et procédures afin de minimiser les risques de problèmes affectant l’environnement opérationnel et la prestation de services aux utilisateurs.",


	    "Expérience": """L'expérience est la connaissance ou la capacité acquise par l'observation ou la participation active. L'expérience s'acquiert en effectuant le travail dans un environnement réel et en passant par différentes situations nécessitant des actions diverses.Des exemples d'expériences incluent : le comptage cyclique, le cross docking, et la gestion des matériaux dangereux.Une liste complète des domaines d'expérience reconnus peut être trouvée à la fin de cette section. Les expériences sont codées dans le cadre SCOR sous "HE.000". (Seule une liste partielle des expériences associées aux compétences SCOR est incluse ici.)""",

	    "Formation": """La formation permet de développer des compétences ou des comportements spécifiques grâce à des instructions. Elle peut inclure des formations formelles, comme SCOR-P, des cours spécialisés ou des apprentissages réalisés directement sur le lieu de travail. Une liste complète des formations reconnues est disponible dans le cadre SCOR, où elles sont codées sous la désignation HT.000. Le texte présenté ici constitue un extrait des formations associées aux compétences SCOR.""",

}
