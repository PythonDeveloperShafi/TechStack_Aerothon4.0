import React from 'react';
import './working.css';

import sites from '../../Assets/sites.png';

const Working = () => {
  return (
    <div className='ts__working section__padding' id='working'>
      <div className='ts__working-image'>
        <img src={sites} alt='sites' />
      </div>
      <div className='ts__working-content'>
        <h1 className='gradient__text'>
          What is the working principle behind the framework
          integration?
        </h1>
        <p>
          Yet bed any for travelling assistance indulgence unpleasing.
          Not thoughts all exercise blessing. Indulgence way
          everything joy alteration boisterous the attachment. Party
          we years to order allow asked of.
        </p>
      </div>
    </div>
  );
};

export default Working;
