import React from "react";
import styles from "./footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className="container-fluid">
        <div className="row justify-content-around">
          <div className="col-8 col-md-5">
            <h5 className={styles.title}>Speak To Me</h5>
            <p className={styles.description}>
              Say whatever you want and I'll hear it.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
export default Footer;