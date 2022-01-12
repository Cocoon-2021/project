use resumedata;
select 
distinct resume.id,
basics.name,
basics.label,
basics.image,
basics_profiles.network,
basics_profiles.username,
basics_profiles.url
from resume inner join basics left join basics_profiles on 
resume.id = basics.resume_id 
and 
resume.id = basics_profiles.resume_id;