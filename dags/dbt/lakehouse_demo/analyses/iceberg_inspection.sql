select * from iceberg.demo.fct_events.snapshots order by committed_at desc;
-- select * from iceberg.demo.fct_events.files;
-- select * from iceberg.demo.fct_events version as of <snapshot_id>;
