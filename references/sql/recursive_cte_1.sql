-- The components of a car.
create table components (
    description varchar,
    component_id integer,
    quantity integer,
    parent_component_id integer
    );

insert into components (description, quantity, component_id, parent_component_id) values
    ('car', 1, 1, 0),
       ('wheel', 4, 11, 1),
          ('tire', 1, 111, 11),
          ('#112 bolt', 5, 112, 11),
          ('brake', 1, 113, 11),
             ('brake pad', 1, 1131, 113),
       ('engine', 1, 12, 1),
          ('piston', 4, 121, 12),
          ('cylinder block', 1, 122, 12),
          ('#112 bolt', 16, 112, 12)   -- Can use same type of bolt in multiple places
    ;
with recursive current_layer (indent, layer_id, parent_component_id, component_id, description, sort_key) as (
  select 
      '...', 
      1, 
      parent_component_id, 
      component_id, 
      description, 
      '0001'
    from components where component_id = 1
  union all
  select indent || '...',
      layer_id + 1,
      components.parent_component_id,
      components.component_id, 
      components.description,
      sort_key || substring('000' || components.component_id, -4)
    from current_layer join components 
      on (components.parent_component_id = current_layer.component_id)
  )
select
  -- The indentation gives us a sort of "side-ways tree" view, with
  -- sub-components indented under their respective components.
  indent || description as description, 
  component_id,
  parent_component_id
  -- The layer_ID and sort_key are useful for debugging, but not
  -- needed in the report.
--  , layer_ID, sort_key
  from current_layer
  order by sort_key;
  
/*
+-------------------------+--------------+---------------------+
| DESCRIPTION             | COMPONENT_ID | PARENT_COMPONENT_ID |
|-------------------------+--------------+---------------------|
| ...car                  |            1 |                   0 |
| ......wheel             |           11 |                   1 |
| .........tire           |          111 |                  11 |
| .........#112 bolt      |          112 |                  11 |
| .........brake          |          113 |                  11 |
| ............brake pad   |         1131 |                 113 |
| ......engine            |           12 |                   1 |
| .........#112 bolt      |          112 |                  12 |
| .........piston         |          121 |                  12 |
| .........cylinder block |          122 |                  12 |
+-------------------------+--------------+---------------------+

*/
