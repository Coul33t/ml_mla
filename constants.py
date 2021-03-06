from tools import Person

implemented_algo = ('k-means', 'dbscan', 'agglomerative', 'mean-shift', 'gmm')

right_joints_list = [['RightHand'],
                     ['RightHand', 'RightForeArm'],
                     ['RightHand', 'RightForeArm', 'RightArm'],
                     ['RightHand', 'RightForeArm', 'RightArm', 'RightShoulder'],
                     ['RightHand', 'RightForeArm', 'RightArm', 'RightShoulder', 'Neck', 'Hips']]

left_joints_list = [['LeftHand'],
                    ['LeftHand', 'LeftForeArm'],
                    ['LeftHand', 'LeftForeArm', 'LeftArm'],
                    ['LeftHand', 'LeftForeArm', 'LeftArm', 'LeftShoulder'],
                    ['LeftHand', 'LeftForeArm', 'LeftArm', 'LeftShoulder', 'Neck', 'Hips']]

neutral_joints_list = [['Hand'],
                       ['Hand', 'ForeArm'],
                       ['Hand', 'ForeArm', 'Arm'],
                       ['Hand', 'ForeArm', 'Arm', 'Shoulder'],
                       ['Hand', 'ForeArm', 'Arm', 'Shoulder', 'Neck', 'Hips']]

data_types_combination = [['BegMaxEndSpeedNorm'],
                          ['BegMaxEndSpeedx',     'BegMaxEndSpeedy',    'BegMaxEndSpeedz'],
                          ['BegMaxEndSpeedDirx',  'BegMaxEndSpeedDiry', 'BegMaxEndSpeedDirz'],
                          ['BegMaxEndSpeedNorm',  'BegMaxEndSpeedx',    'BegMaxEndSpeedy',    'BegMaxEndSpeedz'],
                          ['BegMaxEndSpeedNorm',  'BegMaxEndSpeedDirx', 'BegMaxEndSpeedDiry', 'BegMaxEndSpeedDirz'],
                          ['BegMaxEndSpeedDirx',  'BegMaxEndSpeedDiry', 'BegMaxEndSpeedDirz', 'BegMaxEndSpeedx',    'BegMaxEndSpeedy', 'BegMaxEndSpeedz'],
                          ['BegMaxEndSpeedNorm',  'BegMaxEndSpeedDirx', 'BegMaxEndSpeedDiry', 'BegMaxEndSpeedDirz', 'BegMaxEndSpeedx', 'BegMaxEndSpeedy', 'BegMaxEndSpeedz'],

                          # ['SpeedNorm'],
                          # ['Speedx',    'Speedy',     'Speedz'],
                          # ['SpeedDirx', 'SpeedDiry',  'SpeedDirz'],
                          # ['SpeedNorm', 'Speedx',     'Speedy',     'Speedz'],
                          # ['SpeedNorm', 'SpeedDirx',  'SpeedDiry',  'SpeedDirz'],
                          # ['Speedx',    'Speedy', 'Speedz', 'SpeedDirx',  'SpeedDiry', 'SpeedDirz'],
                          # ['SpeedNorm', 'Speedx', 'Speedy', 'Speedz',     'SpeedDirx', 'SpeedDiry', 'SpeedDirz'],

                          # ['AccelerationNorm'],
                          # ['Accelerationx',     'Accelerationy',    'Accelerationz'],
                          # ['AccelerationDirx',  'AccelerationDiry', 'AccelerationDirz'],
                          # ['AccelerationNorm', 'Accelerationx',     'Accelerationy',    'Accelerationz'],
                          # ['AccelerationNorm', 'AccelerationDirx',  'AccelerationDiry', 'AccelerationDirz'],
                          # ['Accelerationx',     'Accelerationy', 'Accelerationz', 'AccelerationDirx',   'AccelerationDiry',   'AccelerationDirz'],
                          # ['AccelerationNorm',  'Accelerationx', 'Accelerationy', 'Accelerationz',      'AccelerationDirx',   'AccelerationDiry', 'AccelerationDirz'],

                          # ['AccelerationNorm', 'SpeedNorm'],
                          # ['AccelerationNorm', 'BegMaxEndSpeedNorm'],
                          # ['SpeedNorm', 'BegMaxEndSpeedNorm'],
                          # ['AccelerationNorm', 'SpeedNorm', 'BegMaxEndSpeedNorm']
                          ]

people_names_O = [['Aous', 'left'], ['Damien', 'left'], ['Esteban', 'right'], ['Guillaume', 'right'],
                 ['Ines', 'right'], ['Iza', 'right'], ['Ludovic', 'right'], ['Marc', 'right'],
                 ['Oussema', 'right'], ['Pierre', 'right'], ['Sebastien', 'right'],
                 ['Vincent', 'right'], ['Yann', 'right'],
                 [['Aous', 'Damien'], 'left'],
                 [['Esteban', 'Guillaume', 'Ines', 'Iza', 'Ludovic', 'Marc', 'Oussema', 'Pierre', 'Sebastien', 'Vincent', 'Yann'], 'right']]


people_names = [['Aous', 'left'], ['Damien', 'left'], ['Esteban', 'right'], ['Guillaume', 'right'],
                ['Ines', 'right'], ['Iza', 'right'], ['Ludovic', 'right'], ['Marc', 'right'],
                ['Oussema', 'right'], ['Pierre', 'right'], ['Sebastien', 'right'],
                ['Vincent', 'right'], ['Yann', 'right']]

names_labels = {'Aous': 'AKARAOUI_LABELS_2',
                'Damien': 'DBRUN_LABELS_2',
                'Esteban': 'ELOISEAU_LABELS_2',
                'Guillaume': 'GLOUP_LABELS_2',
                'Ines': 'IDABBEBI_LABELS_2',
                'Iza': 'IMARFISI_LABELS_2',
                'Ludovic': 'LHAMON_LABELS_2',
                'Marc': 'MLECONTE_LABELS_2',
                'Oussema': 'OMAHDI_LABELS_2',
                'Pierre': 'PLAFORCADE_LABELS_2',
                'Sebastien': 'SGEORGE_LABELS_2',
                'Vincent': 'VBETTENFELD_LABELS_2',
                'Yann': 'YWALKOWIAK_LABELS_2'}

joints_name_corres = {'LeftHand': 'LH', 'LeftForeArm': 'LFA', 'LeftArm': 'LA', 'LeftShoulder': 'LS',
                      'RightHand': 'RH', 'RightForeArm': 'RFA', 'RightArm': 'RA', 'RightShoulder': 'RS',
                      'Hand': 'H', 'ForeArm': 'FA', 'Arm': 'A', 'Shoulder': 'S',
                      'Neck': 'N', 'Hips': 'H'}

data_types_corres = {'BegMaxEndSpeedNorm_BegMaxEndSpeedx_BegMaxEndSpeedy_BegMaxEndSpeedz': 'BegMaxEndSpeedNormxyz',
                     'BegMaxEndSpeedNormBegMaxEndSpeedxBegMaxEndSpeedyBegMaxEndSpeedz': 'BegMaxEndSpeedNormxyz',

                     'BegMaxEndSpeedx_BegMaxEndSpeedy_BegMaxEndSpeedz': 'BegMaxEndSpeedxyz',
                     'BegMaxEndSpeedxBegMaxEndSpeedyBegMaxEndSpeedz': 'BegMaxEndSpeedxyz',

                     'BegMaxEndSpeedDirx_BegMaxEndSpeedDiry_BegMaxEndSpeedDirz': 'BegMaxEndSpeedDirxyz',
                     'BegMaxEndSpeedDirxBegMaxEndSpeedDiryBegMaxEndSpeedDirz': 'BegMaxEndSpeedDirxyz',

                     'AccelerationNorm_Accelerationx_Accelerationy_Accelerationz': 'AccelerationNormxyz',
                     'AccelerationNormAccelerationxAccelerationyAccelerationz': 'AccelerationNormxyz',

                     'Accelerationx_Accelerationy_Accelerationz': 'Accelerationxyz',
                     'AccelerationxAccelerationyAccelerationz': 'Accelerationxyz',

                     'SpeedDirx_SpeedDiry_SpeedDirz': 'SpeedDirxyz',
                     'SpeedDirxSpeedDirySpeedDirz': 'SpeedDirxyz',

                     'AccelerationDirx_AccelerationDiry_AccelerationDirz': 'AccDirxyz',
                     'AccelerationDirxAccelerationDiryAccelerationDirz': 'AccDirxyz',

                     'Dirx_Diry_Dirz': 'Dirxyz',
                     'DirxDiryDirz': 'Dirxyz',

                     'Speedx_Speedy_Speedz': 'Speedxyz',
                     'SpeedxSpeedySpeedz': 'Speedxyz',

                     'BegMaxEndSpeed': 'BMES',
                     'Acceleration': 'Acc'}

data_types_base_name = ['BegMaxEndSpeed', 'Speed', 'Acceleration']


problems_and_advices = {'leaning': "Your shoulders shouldn't move when you're throwing.",
                        'javelin': "Your throwing hand should always be in front of you when you're throwing.",
                        'align_arm': "Your arm should stay aligned regarding to your body.",
                        'elbow_move': "Your elbow shouldn't move while you're throwing."}

problemes_et_solutions = {'leaning': "Votre corps et vos épaules ne doivent pas bouger pendant votre lancer.",
                          'javelin': "Votre main doit toujours rester devant votre corps lorsque vous lancez.",
                          'align_arm': "Votre bras doit rester aligné (de la main à l'épaule) lorsque vous lancez.",
                          'elbow_move': "Votre coude ne doit pas bouger lors du lancer."}

old_students_list = [Person(r'', 'PonroyL', 'Right', 'Ponroy_Loris'),
                     Person(r'', 'YanisS', 'Right', 'Saupin_Yanis'),
                     Person(r'', 'DoneauR', 'Right', 'Doneau_Rafael'),
                     Person(r'', 'JametB', 'Right', 'Jamet_Baptiste'),
                     Person(r'', 'PlautF', 'Left', 'Plaut_Florian'),
                     Person(r'', 'CorgniardA', 'Right', 'Corgniard_Antoine'),
                     Person(r'', 'MaurinM', 'Right', 'Maurin_Maxime'),
                     Person(r'', 'LivainC', 'Right', 'Livain_Corentin'),
                     Person(r'', 'AubertJ', 'Right', 'Aubert_Julian'),
                     Person(r'', 'ClouetA', 'Right', 'Clouet_Alexandre'),
                     Person(r'', 'LechatW', 'Right', 'Lechat_William'),
                     Person(r'', 'BrouardS', 'Right', 'Brouard_Samuel'),
                     Person(r'', 'SicardT', 'Right', 'Sicard_Teddy'),
                     Person(r'', 'LefortN', 'Right', 'Lefort_Nathan'),
                     Person(r'', 'BlanchardA', 'Right', 'Blanchard_Axel'),
                     Person(r'', 'GuideauL', 'Right', 'Guideau_Lucas'),
                     Person(r'', 'AudrezetR', 'Right', 'Audrezet_Remi'),
                     Person(r'', 'KherratiY', 'Right', 'Kherrati_Yazid'),
                     Person(r'', 'LeborgneA', 'Right', 'Leborgne_Alex'),
                     Person(r'', 'PoissonneauT', 'Right', 'Poissonneau_Theo'),
                     Person(r'', 'BrunetL', 'Right', 'Brunet_Leo'),
                     Person(r'', 'BellonG', 'Right', 'Bellon_Gregoire'),
                     Person(r'', 'PegeC', 'Right', 'Pege_Charly'),
                     Person(r'', 'EuvrardL', 'Right', 'Euvrard_Louis'),
                     Person(r'', 'DurandN', 'Left', 'Durand_Nicolas'),
                     Person(r'', 'BoussardC', 'Right', 'Boussard_Clement'),
                     Person(r'', 'RouxelV', 'Right', 'Rouxel_Valentin'),
                     Person(r'', 'CaillonC', 'Right', 'Caillon_Charles'),
                     Person(r'', 'DucheminT', 'Right', 'Duchemin_Thomas'),
                     Person(r'', 'DelhommaisT', 'Right', 'Delhommais_Tony'),
                     Person(r'', 'RobertF', 'Left', 'Robert_Flavien'),
                     Person(r'', 'BettenfeldV', 'Right', 'Bettenfeld_Vincent'),
                     Person(r'', 'DizelC', 'Right', 'Dizel_Corentin'),
                     Person(r'', 'ValadonH', 'Right', 'Valadon_Hugo'),
                     Person(r'', 'PechinS', 'Right', 'Pechin_Salome'),
                     Person(r'', 'HuetL', 'Right', 'Huet_Loic'),
                     Person(r'', 'SallesW', 'Left', 'Salles_Wilhelm'),
                     Person(r'', 'MaletL', 'Right', 'Malet_Leo'),
                     Person(r'', 'BouligandC', 'Right', 'Bouligand_Colin'),
                     Person(r'', 'CoulonA', 'Right', 'Coulon_Axel'),
                     Person(r'', 'GriveauT', 'Right', 'Griveau_Timothee'),
                     Person(r'', 'JonardA', 'Right', 'Jonard_Antoine'),
                     Person(r'', 'BeaussierS', 'Right', 'Beaussier_Simon'),
                     Person(r'', 'DuporgeA', 'Right', 'Duporge_Adrien'),
                     Person(r'', 'LaghouaoutaY', 'Right', 'Laghouaouta_Youness')]


new_students_list = [Person(r'', 'DoneauR', 'Right', 'Doneau_Rafael'), #GR 1
                     Person(r'', 'CorgniardA', 'Right', 'Corgniard_Antoine'),
                     Person(r'', 'AubertJ', 'Right', 'Aubert_Julian'),
                     Person(r'', 'BrouardS', 'Right', 'Brouard_Samuel'),
                     Person(r'', 'BlanchardA', 'Right', 'Blanchard_Axel'),
                     Person(r'', 'KherratiY', 'Right', 'Kherrati_Yazid'),
                     Person(r'', 'BrunetL', 'Right', 'Brunet_Leo'),
                     Person(r'', 'EuvrardL', 'Right', 'Euvrard_Louis'),
                     Person(r'', 'RouxelV', 'Right', 'Rouxel_Valentin'),
                     Person(r'', 'DelhommaisT', 'Right', 'Delhommais_Tony'),
                     Person(r'', 'DizelC', 'Right', 'Dizel_Corentin'),
                     Person(r'', 'HuetL', 'Right', 'Huet_Loic'),
                     Person(r'', 'BouligandC', 'Right', 'Bouligand_Colin'),
                     Person(r'', 'JonardA', 'Right', 'Jonard_Antoine'),
                     Person(r'', 'LaghouaoutaY', 'Right', 'Laghouaouta_Youness'),
                     Person(r'', 'FromontM', 'Right', 'Fromont_Maxime'), # GR 2
                     Person(r'', 'LiguetA', 'Right', 'Liguet_Arthur'),
                     Person(r'', 'DebouvriesA', 'Right', 'Debouvries_Adrien'),
                     Person(r'', 'BancelG', 'Right', 'Bancel_Gilles'),
                     Person(r'', 'HalletV', 'Right', 'Hallet_Valentin'),
                     Person(r'', 'LeMoanV', 'Right', 'LeMoan_Victor'),
                     Person(r'', 'SeniowE', 'Right', 'Seniow_Etienne'),
                     Person(r'', 'MeslinR', 'Right', 'Meslin_Romain'),
                     Person(r'', 'PaumierA', 'Right', 'Paumier_Antoine'),
                     Person(r'', 'BertinA', 'Right', 'Bertin_Arthur'),
                     Person(r'', 'CherbonnierC', 'Right', 'Cherbonnier_Clement'),
                     Person(r'', 'EddeG', 'Right', 'Edde_Gabriel'),
                     Person(r'', 'LeMoanN', 'Right', 'LeMoan_Nathan'),
                     Person(r'', 'MousseF', 'Right', 'Mousse_Florian'),
                     Person(r'', 'DeshayesE', 'Right', 'Deshayes_Elliot'),
                     Person(r'', 'GuezQ', 'Right', 'Guez_Quentin'), # GR 3
                     Person(r'', 'RannouP', 'Right', 'Rannou_Pierre'),
                     Person(r'', 'DerouinT', 'Right', 'Derouin_Thibault'),
                     Person(r'', 'TrochonA', 'Right', 'Trochon_Arthur'),
                     Person(r'', 'BuonL', 'Right', 'Buon_Lea'),
                     Person(r'', 'CornoA', 'Right', 'Corno_Alban'),
                     Person(r'', 'RobertE', 'Right', 'Robert_Emmanuel'),
                     Person(r'', 'GuillemainM', 'Right', 'Guillemain_Maxime'),
                     Person(r'', 'RamilisonJL', 'Right', 'Ramilision_JeanLuc'),
                     Person(r'', 'BaronA', 'Right', 'Baron_Alexandre'),
                     Person(r'', 'DuboisS', 'Right', 'Dubois_Simon'),
                     Person(r'', 'ChambrinN', 'Right', 'Chambrin_Nathan'),
                     Person(r'', 'FourierQ', 'Right', 'Fourier_Quentin'),
                     Person(r'', 'PamatungT', 'Right', 'Pamatung_Thomas'),
                     Person(r'', 'AcharddlVG', 'Right', 'AcharddlV_Gael')]