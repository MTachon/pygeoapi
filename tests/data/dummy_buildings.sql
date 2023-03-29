CREATE SCHEMA IF NOT EXISTS dummy AUTHORIZATION postgres;

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA dummy;

CREATE TABLE IF NOT EXISTS dummy.buildings(
    gid serial PRIMARY KEY,
    centroid geometry(POINT, 25833),
    contours geometry(POLYGON, 25833)
);

INSERT INTO dummy.buildings(centroid, contours)
VALUES ('POINT (473449 7463146)',
        'POLYGON ((473447.9967755177 7463140.685534775, 473453.51980463834 7463143.029921546, 473450.0032244818 7463151.314465227, 473444.4801953612 7463148.970078456, 473447.9967755177 7463140.685534775))'),
    ('POINT (473458 7463104)',
     'POLYGON ((473460.9359104787 7463106.762323238, 473457.1106914547 7463107.931810057, 473455.06408952177 7463101.237676765, 473458.88930854574 7463100.068189946, 473460.9359104787 7463106.762323238))'),
    ('POINT (473446 7463144)',
     'POLYGON ((473446.09474694915 7463138.853056925, 473450.31999101397 7463146.79958526, 473445.9052530499 7463149.146943075, 473441.6800089851 7463141.20041474, 473446.09474694915 7463138.853056925))'),
    ('POINT (473449 7463142)',
     'POLYGON ((473452.3381955018 7463138.820935548, 473452.65221123956 7463144.812712757, 473445.6618044963 7463145.179064451, 473445.3477887586 7463139.187287242, 473452.3381955018 7463138.820935548))'),
    ('POINT (473443 7463137)',
     'POLYGON ((473447.7083111685 7463135.5571535295, 473440.9159249468 7463141.46168479, 473438.2916888306 7463138.44284647, 473445.0840750523 7463132.538315209, 473447.7083111685 7463135.5571535295))'),
    ('POINT (473433 7463125)',
     'POLYGON ((473432.73905580025 7463120.082489641, 473436.8249702975 7463128.10154836, 473433.2609442007 7463129.917510359, 473429.1750297034 7463121.898451641, 473432.73905580025 7463120.082489641))'),
    ('POINT (473451 7463140)',
     'POLYGON ((473454.99435667787 7463139.456755368, 473453.4959303038 7463143.165490787, 473447.00564332213 7463140.543244633, 473448.5040696962 7463136.834509214, 473454.99435667787 7463139.456755368))'),
    ('POINT (473438 7463144)',
     'POLYGON ((473438.99554283824 7463137.7143898895, 473444.28561010957 7463144.995542839, 473437.00445716083 7463150.28561011, 473431.7143898895 7463143.00445716, 473438.99554283824 7463137.7143898895))'),
    ('POINT (473474 7463101)',
     'POLYGON ((473474.83006438427 7463097.491297516, 473477.55805782415 7463100.416712323, 473473.1699356148 7463104.508702483, 473470.441942174 7463101.583287676, 473474.83006438427 7463097.491297516))'),
    -- gid 10
    (NULL,
     'POLYGON ((473464.1495667333 7463116.574655892, 473461.1307284124 7463119.1988920085, 473457.85043326765 7463115.425344108, 473460.8692715885 7463112.8011079915, 473464.1495667333 7463116.574655892))'),
    -- gid 11
    ('POINT (473461 7463116)',
     NULL),
    -- gid 12
    (NULL,
     NULL);
