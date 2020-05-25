import React from "react";
import styles from "./footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className="container-fluid">
        <div className="row justify-content-around">
          <div className="col-8 col-md-5">
            <h5 className={styles.title}>Speak Easy</h5>
            <p className={styles.description}>
              Say whatever you want and I'll hear it.
            </p>
          </div>
          <div className="col-2">
            <ul className="list-unstyled">
              <li>
                <a href="https://github.com/apastel" target="_blank" rel="noopener noreferrer"><i className="icon-github"></i></a>
              </li>
              <li>
                <a className={styles.footerlink} href="/">
                  Example Link
                </a>
              </li>
              <li>
                <a className={styles.footerlink} href="/">
                  Example Link
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
}
export default Footer;