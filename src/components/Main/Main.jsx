import React from "react";
import axios from "axios";
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
    event.preventDefault();
    const response = await axios({
      method: 'post',
      url: '/api/submit',
      data: this.state.value,
      headers: {
        'Content-Type': 'text/plain',
      }
    })
    this.setState({value: ''})
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
                Whatever you type in here will be spoken out loud in my room and displayed on an LED screen.
              </Grid>
              <Grid item xs={12}>
                <TextField
                  id="outlined-basic"
                  label="What do you want it to say?"
                  variant="outlined"
                  onChange={this.handleChange}
                  fullWidth
                  inputProps={{ maxLength: 200 }}
                  value={this.state.value}
                />
              </Grid>
              <Grid item>
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  disabled={!this.state.value.length}
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
