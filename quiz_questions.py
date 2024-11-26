from dataclasses import dataclass
from typing import List

@dataclass
class Question:
    text: str
    choices: List[str]
    correct_answer: int

Questions = [
    Question(
        "Que signifie SCOR dans le contexte de la chaîne logistique?",
        ["Supply Chain Operations Reference",
         "Strategic Chain Optimization Review",
         "Supply Chain Optimization Resources",
         "System Chain Operations Rotation"],
        0
    ),
    Question(
        "Quel processus SCOR concerne la planification des activités de la chaîne logistique?",
        ["Source", "Make", "Plan", "Deliver"],
        2
    ),
    Question(
        "Quel niveau du modèle SCOR définit les processus de base?",
        ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4"],
        0
    ),
    Question(
        "Quelle métrique SCOR mesure la fiabilité de la livraison?",
        ["Perfect Order Fulfillment",
         "Order Cycle Time",
         "Cost of Goods Sold",
         "Inventory Days of Supply"],
        0
    ),
    Question(
        "Quel processus SCOR est responsable de la gestion des retours?",
        ["Make", "Source", "Deliver", "Return"],
        3
    ),
    Question(
        "Quel processus SCOR est responsable de la production de biens ou services?",
        ["Plan", "Make", "Deliver", "Return"],
        1
    ),
    Question(
        "Quel niveau SCOR fournit une vue stratégique des processus?",
        ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4"],
        0
    ),
    Question(
        "Quel processus SCOR gère la gestion des retours des clients?",
        ["Plan", "Deliver", "Return", "Enable"],
        2
    ),
    Question(
        "Quelle est l'utilité principale du processus SCOR Plan?",
        ["Coordonner les activités de la chaîne",
         "Produire des biens",
         "Gérer les retours",
         "Livrer aux clients"],
        0
    ),
    Question(
        "Quel processus SCOR s’occupe de la relation avec les fournisseurs?",
        ["Make", "Source", "Return", "Plan"],
        1
    ),
    Question(
        "Quelle métrique mesure le pourcentage des commandes livrées parfaitement?",
        ["Order Fill Rate",
         "Perfect Order Fulfillment",
         "Order Cycle Time",
         "Cost of Goods Sold"],
        1
    ),
    Question(
        "Quel indicateur SCOR mesure le temps entre la commande et la livraison?",
        ["Perfect Order Fulfillment", "Order Fill Rate", "Order Cycle Time", "Agility"],
        2
    ),
    Question(
        "Quelle est la priorité du processus Deliver dans SCOR?",
        ["Planifier les commandes",
         "Assurer la livraison des produits",
         "Gérer les stocks",
         "Retourner les produits défectueux"],
        1
    ),
    Question(
        "Quel processus SCOR vise à soutenir les autres processus?",
        ["Enable", "Source", "Make", "Deliver"],
        0
    ),
    Question(
        "Quel niveau SCOR décrit les étapes détaillées des tâches?",
        ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4"],
        2
    ),
    Question(
        "Quelle métrique SCOR mesure la flexibilité dans la chaîne logistique?",
        ["Agility", "Order Cycle Time", "Cost of Goods Sold", "Perfect Order Fulfillment"],
        0
    ),
    Question(
        "Quelle métrique SCOR mesure les coûts de la chaîne logistique?",
        ["Inventory Days of Supply", "Order Fill Rate", "Cost of Goods Sold", "Order Cycle Time"],
        2
    ),
    Question(
        "Quel processus SCOR est associé à l'achat de matériaux?",
        ["Source", "Plan", "Deliver", "Enable"],
        0
    ),
    Question(
        "Quel indicateur mesure la précision des prévisions dans SCOR?",
        ["Forecast Accuracy", "Order Fill Rate", "Agility", "Cash-to-Cash Cycle Time"],
        0
    ),
    Question(
        "Quelle métrique évalue la rapidité des réponses aux changements de la demande?",
        ["Responsiveness", "Agility", "Perfect Order Fulfillment", "Order Fill Rate"],
        1
    ),
    Question(
        "Quelle étape SCOR traite des produits défectueux retournés par les clients?",
        ["Source", "Deliver", "Return", "Plan"],
        2
    ),
    Question(
        "Quelle métrique SCOR mesure le temps de cycle entre le paiement et l'encaissement?",
        ["Cash-to-Cash Cycle Time",
         "Order Cycle Time",
         "Cost of Goods Sold",
         "Agility"],
        0
    ),
    Question(
        "Quel processus SCOR aide à planifier les niveaux d’inventaire?",
        ["Plan", "Source", "Make", "Enable"],
        0
    ),
    Question(
        "Quelle métrique évalue le niveau de service client dans SCOR?",
        ["Order Fill Rate", "Perfect Order Fulfillment", "Inventory Accuracy", "Responsiveness"],
        1
    ),
    Question(
        "Quel processus SCOR optimise les stocks et la planification des ressources?",
        ["Plan", "Source", "Make", "Deliver"],
        0
    ),
    Question(
        "Quel niveau SCOR relie le cadre théorique aux opérations spécifiques?",
        ["Niveau 3", "Niveau 4", "Niveau 1", "Niveau 2"],
        1
    ),
    Question(
        "Quel processus SCOR s'assure que les produits arrivent au client final?",
        ["Deliver", "Make", "Source", "Return"],
        0
    ),
    Question(
        "Quelle métrique SCOR mesure les jours d'approvisionnement en inventaire?",
        ["Inventory Days of Supply",
         "Order Cycle Time",
         "Perfect Order Fulfillment",
         "Cost of Goods Sold"],
        0
    ),
    Question(
        "Quel processus SCOR coordonne la chaîne logistique globale?",
        ["Plan", "Enable", "Source", "Deliver"],
        0
    ),
    Question(
        "Quel processus SCOR vise à gérer les capacités de production?",
        ["Plan", "Make", "Source", "Deliver"],
        1
    ),
    Question(
        "Quelle métrique SCOR mesure la vitesse de transformation des matériaux?",
        ["Order Cycle Time", "Production Lead Time", "Agility", "Perfect Order Fulfillment"],
        1
    ),
    Question(
        "Quel niveau SCOR décrit les processus interentreprises?",
        ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4"],
        1
    ),
    Question(
        "Quelle étape SCOR est essentielle pour réduire les délais de livraison?",
        ["Make", "Source", "Deliver", "Plan"],
        2
    ),
    Question(
        "Quel processus SCOR est associé à l'identification des fournisseurs stratégiques?",
        ["Source", "Plan", "Enable", "Make"],
        0
    ),
    Question(
        "Quelle métrique SCOR évalue la capacité à répondre aux variations de demande?",
        ["Agility", "Perfect Order Fulfillment", "Order Fill Rate", "Cost of Goods Sold"],
        0
    ),
    Question(
        "Quel indicateur SCOR mesure le coût des retours?",
        ["Cost of Returns", "Perfect Order Fulfillment", "Agility", "Order Cycle Time"],
        0
    ),
    Question(
        "Quelle est la fonction principale du processus Enable dans SCOR?",
        ["Supporter les autres processus",
         "Livrer les produits aux clients",
         "Produire les biens",
         "Retourner les produits"],
        0
    ),
    Question(
        "Quel niveau SCOR est le plus détaillé?",
        ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4"],
        3
    ),
    Question(
        "Quel processus SCOR est directement lié au transport des produits?",
        ["Plan", "Deliver", "Return", "Enable"],
        1
    ),
    Question(
        "Quelle métrique SCOR est utilisée pour évaluer l’efficacité des prévisions?",
        ["Forecast Accuracy", "Order Fill Rate", "Agility", "Cost of Goods Sold"],
        0
    ),
    Question(
        "Quel processus SCOR est responsable de la gestion des matières premières?",
        ["Source", "Make", "Deliver", "Plan"],
        0
    ),
    Question(
        "Quelle métrique SCOR évalue la précision de l'inventaire?",
        ["Inventory Accuracy", "Perfect Order Fulfillment", "Order Fill Rate", "Agility"],
        0
    ),
    Question(
        "Quelle étape SCOR vise à améliorer la coordination des flux financiers?",
        ["Plan", "Deliver", "Enable", "Return"],
        2
    ),
    Question(
        "Quel processus SCOR est crucial pour réduire les coûts d'exploitation?",
        ["Plan", "Enable", "Deliver", "Return"],
        0
    ),
    Question(
        "Quelle métrique SCOR mesure la flexibilité à gérer des produits spécifiques?",
        ["Agility", "Order Cycle Time", "Inventory Accuracy", "Perfect Order Fulfillment"],
        0
    ),
    Question(
        "Quel processus SCOR inclut la production et le contrôle qualité?",
        ["Make", "Plan", "Deliver", "Return"],
        0
    ),
    Question(
        "Quelle étape SCOR soutient l’intégration des technologies?",
        ["Enable", "Plan", "Deliver", "Source"],
        0
    ),
    Question(
        "Quel processus SCOR permet de surveiller les performances des fournisseurs?",
        ["Source", "Deliver", "Return", "Plan"],
        0
    ),
    Question(
        "Quelle métrique SCOR calcule le pourcentage d'inventaire utilisé dans une période donnée?",
        ["Inventory Turnover", "Inventory Accuracy", "Order Fill Rate", "Cost of Goods Sold"],
        0
    )
]
