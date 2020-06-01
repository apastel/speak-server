import React from "react";
import { TextField, Button, Grid } from "@material-ui/core"

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  async handleSubmit(event) {
    const response = await fetch('/submit', {
      method: 'POST',
      body: this.state.value,
      headers: {
        'Content-Type': 'text/plain'
      }
    })
    return response.ok
  }

  render() {
    return <main id="mainContent">
      <div className="container">
        <div className="row justify-content-center mt-5 p-0">
          <form onSubmit={this.handleSubmit}>
            <Grid 
              container
              direction="column"
              justify="center"
              alignItems="center"
              spacing={2}
            >
              <Grid item xs={12}>
                <TextField
                  id="outlined-basic"
                  label="What do you want it to say?"
                  variant="outlined"
                  onChange={this.handleChange}
                  fullWidth
                />
              </Grid>
              <Grid item>
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                >
                  Speak
                </Button>
              </Grid>
            </Grid>
          </form>
        </div>
      </div>
    </main>;
  }
}
export default Main;
