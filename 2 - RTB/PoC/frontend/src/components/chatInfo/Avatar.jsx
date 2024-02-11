import React from "react";

export default function Avatar(props) {

  return (
    <div className="avatar">
      <div className="avatar-img">
        {props.image}
      </div>
    </div>
  )
}
